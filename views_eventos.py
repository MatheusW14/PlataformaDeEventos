import time
import json
from flask import (
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
    send_from_directory,
    current_app,
)
from lista_eventos import app, db
from models import Eventos, Usuarios, Participantes
from helpers import recupera_imagem, deleta_arquivo, FormularioEvento


@app.route("/")
def index():
    lista = Eventos.query.order_by(Eventos.id)

    usuario_logado = None
    if "usuario_logado" in session and session["usuario_logado"] is not None:
        usuario_logado = Usuarios.query.filter_by(
            nickname=session["usuario_logado"]
        ).first()

    return render_template(
        "lista.html", titulo="Eventos", eventos=lista, usuario=usuario_logado
    )


@app.route("/novo")
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        return redirect(url_for("login", proxima=url_for("novo")))
    form = FormularioEvento()
    return render_template("novo.html", titulo="Novo Evento", form=form)


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    form = FormularioEvento(request.form)

    if not form.validate_on_submit():
        flash("Erro no formulário, por favor verifique os dados.", "danger")
        return redirect(url_for("novo"))

    nome = form.nome.data
    data = form.data.data
    tema = form.tema.data
    descricao = form.descricao.data

    evento = Eventos.query.filter_by(nome=nome).first()

    if evento:
        flash("Evento com este nome já existe!", "warning")
        return redirect(url_for("index"))

    novo_evento = Eventos(nome=nome, data=data, tema=tema, descricao=descricao)
    db.session.add(novo_evento)

    participantes_data = form.participantes_manuais.data or ""
    try:
        tags = json.loads(participantes_data)
        nomes_participantes = [tag["value"] for tag in tags]
    except (json.JSONDecodeError, TypeError):
        nomes_participantes = [
            nome.strip() for nome in participantes_data.split(",") if nome.strip()
        ]

    for nome_participante in nomes_participantes:
        participante = Participantes(nome=nome_participante, evento=novo_evento)
        db.session.add(participante)

    db.session.commit()

    arquivo = request.files["arquivo"]
    if arquivo.filename:
        upload_path = current_app.config["UPLOAD_PATH"]
        timestamp = time.time()
        arquivo.save(f"{upload_path}/capa{novo_evento.id}-{timestamp}.jpg")

    flash("Evento criado com sucesso!", "success")
    return redirect(url_for("index"))


@app.route("/editar/<int:id>")
def editar(id):
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        return redirect(url_for("login", proxima=url_for("editar", id=id)))

    evento = Eventos.query.get_or_404(id)
    form = FormularioEvento(obj=evento)

    nomes_participantes = [p.nome for p in evento.participantes]
    form.participantes_manuais.data = ",".join(nomes_participantes)

    capa_evento = recupera_imagem(id)
    return render_template(
        "editar.html",
        titulo="Editando Evento",
        id=id,
        capa_evento=capa_evento,
        form=form,
    )


@app.route(
    "/atualizar",
    methods=[
        "POST",
    ],
)
def atualizar():
    form = FormularioEvento(request.form)

    if form.validate_on_submit():
        evento = Eventos.query.get_or_404(request.form["id"])
        evento.nome = form.nome.data
        evento.data = form.data.data
        evento.tema = form.tema.data
        evento.descricao = form.descricao.data

        evento.participantes.clear()
        participantes_data = form.participantes_manuais.data or ""
        try:
            tags = json.loads(participantes_data)
            nomes_participantes = [tag["value"] for tag in tags]
        except (json.JSONDecodeError, TypeError):
            nomes_participantes = [
                nome.strip() for nome in participantes_data.split(",") if nome.strip()
            ]

        for nome_participante in nomes_participantes:
            participante = Participantes(nome=nome_participante, evento=evento)
            db.session.add(participante)

        db.session.commit()

        arquivo = request.files["arquivo"]
        if arquivo.filename:
            deleta_arquivo(evento.id)
            upload_path = current_app.config["UPLOAD_PATH"]
            timestamp = time.time()
            arquivo.save(f"{upload_path}/capa{evento.id}-{timestamp}.jpg")

        flash("Evento atualizado com sucesso!", "success")

    return redirect(url_for("index"))


@app.route("/deletar/<int:id>")
def deletar(id):
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        return redirect(url_for("login"))

    deleta_arquivo(id)
    Eventos.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Evento deletado com sucesso!", "danger")

    return redirect(url_for("index"))


@app.route("/uploads/<nome_arquivo>")
def imagem(nome_arquivo):
    return send_from_directory(current_app.config["UPLOAD_PATH"], nome_arquivo)


@app.route(
    "/participar/<int:id>",
    methods=[
        "POST",
    ],
)
def participar(id):
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        flash("Você precisa estar logado para participar.", "danger")
        return redirect(url_for("login"))

    evento = Eventos.query.get_or_404(id)
    nickname_logado = session["usuario_logado"]

    participante_existente = Participantes.query.filter_by(
        evento_id=evento.id, nome=nickname_logado
    ).first()

    if participante_existente:
        flash("Você já está participando deste evento!", "info")
    else:
        novo_participante = Participantes(nome=nickname_logado, evento_id=evento.id)
        db.session.add(novo_participante)
        db.session.commit()
        flash("Sua participação foi confirmada!", "success")

    return redirect(url_for("index"))


@app.route(
    "/desinscrever/<int:id>",
    methods=[
        "POST",
    ],
)
def desinscrever(id):
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        flash("Você precisa estar logado para realizar esta ação.", "danger")
        return redirect(url_for("login"))

    nickname_logado = session["usuario_logado"]

    participante_para_remover = Participantes.query.filter_by(
        evento_id=id, nome=nickname_logado
    ).first()

    if participante_para_remover:
        db.session.delete(participante_para_remover)
        db.session.commit()
        flash("Você saiu do evento.", "success")
    else:
        flash("Você não estava participando deste evento.", "info")

    return redirect(url_for("index"))
