from lista_eventos import app, db, bcrypt
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioCadastro
from flask_bcrypt import check_password_hash


@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    form = FormularioUsuario()
    return render_template("login.html", proxima=proxima, form=form)


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    if usuario:
        if bcrypt.check_password_hash(usuario.senha, form.senha.data):
            session["usuario_logado"] = usuario.nickname
            flash(usuario.nickname + " logado com sucesso!")
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)

    flash("Falha no login. Verifique seu usuário e senha.")
    return redirect(url_for("login"))


@app.route("/cadastro")
def cadastro():
    form = FormularioCadastro()
    return render_template("cadastro.html", titulo="Cadastre-se", form=form)


@app.route(
    "/registrar",
    methods=[
        "POST",
    ],
)
def registrar():
    form = FormularioCadastro(request.form)

    if not form.validate_on_submit():
        flash("Erro no formulário. Por favor, verifique os dados.")
        return redirect(url_for("cadastro"))

    nome = form.nome.data
    nickname = form.nickname.data
    senha = form.senha.data

    usuario = Usuarios.query.filter_by(nickname=nickname).first()
    if usuario:
        flash(f'O usuário "{nickname}" já está em uso!')
        return redirect(url_for("cadastro"))

    senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")
    novo_usuario = Usuarios(nome=nome, nickname=nickname, senha=senha_hash)

    db.session.add(novo_usuario)
    db.session.commit()

    flash(f"Usuário {nickname} cadastrado com sucesso!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for("index"))
