from lista_eventos import db


class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    tema = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.name
