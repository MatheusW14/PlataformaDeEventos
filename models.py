from lista_eventos import db


class Participantes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey("eventos.id"), nullable=False)

    def __repr__(self):
        return f"<Participante {self.nome}>"


class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)
    tema = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    participantes = db.relationship(
        "Participantes", backref="evento", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Evento {self.nome}>"


class Usuarios(db.Model):
    nickname = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
