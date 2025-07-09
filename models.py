from lista_eventos import db


participantes_eventos = db.Table(
    "participantes",
    db.Column(
        "usuario_nickname",
        db.String(20),
        db.ForeignKey("usuarios.nickname"),
        primary_key=True,
    ),
    db.Column("evento_id", db.Integer, db.ForeignKey("eventos.id"), primary_key=True),
)


class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)
    tema = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    participantes = db.relationship(
        "Usuarios",
        secondary=participantes_eventos,
        lazy="subquery",
        back_populates="eventos_participando",
    )

    def __repr__(self):
        return f"<Evento {self.nome}>"


class Usuarios(db.Model):
    nickname = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    eventos_participando = db.relationship(
        "Eventos",
        secondary=participantes_eventos,
        lazy=True,
        back_populates="participantes",
    )

    def __repr__(self):
        return f"<Usuario {self.nome}>"
