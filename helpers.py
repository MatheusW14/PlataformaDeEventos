import os
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    validators,
    DateField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, EqualTo


class FormularioEvento(FlaskForm):
    nome = StringField(
        "Nome do Evento", [validators.DataRequired(), validators.Length(min=1, max=50)]
    )
    data = DateField("Data do Evento", [validators.DataRequired()], format="%Y-%m-%d")
    tema = StringField(
        "Tema", [validators.DataRequired(), validators.Length(min=1, max=40)]
    )
    descricao = TextAreaField(
        "Descrição", [validators.DataRequired(), validators.Length(min=1, max=200)]
    )
    salvar = SubmitField("Salvar")


class FormularioUsuario(FlaskForm):
    nickname = StringField(
        "Usuário", [validators.DataRequired(), validators.Length(min=1, max=8)]
    )
    senha = PasswordField(
        "Senha", [validators.DataRequired(), validators.Length(min=1, max=100)]
    )
    login = SubmitField("Login")


class FormularioCadastro(FlaskForm):
    nome = StringField("Nome Completo", [DataRequired(), Length(min=1, max=20)])
    nickname = StringField("Usuário", [DataRequired(), Length(min=1, max=8)])
    senha = PasswordField(
        "Senha",
        [
            DataRequired(),
            Length(min=4, max=100),
            EqualTo("confirma_senha", message="As senhas devem ser iguais"),
        ],
    )
    confirma_senha = PasswordField("Confirmação de Senha")
    cadastrar = SubmitField("Cadastrar")


def recupera_imagem(id):
    for nome_arquivo in os.listdir(current_app.config["UPLOAD_PATH"]):
        if f"capa{id}" in nome_arquivo:
            return nome_arquivo

    return "capa_padrao.jpg"


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != "capa_padrao.jpg":
        os.remove(os.path.join(current_app.config["UPLOAD_PATH"], arquivo))
