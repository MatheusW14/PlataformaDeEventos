from lista_eventos import db


class Participantes(db.Model):
    """
    Participantes Model
    Represents a participant in an event.
    Attributes:
        id (int): The unique identifier for the participant.
        nome (str): The name of the participant. This field is required and has a maximum length of 100 characters.
        evento_id (int): The foreign key linking the participant to an event. This field is required.
    Methods:
        __repr__(): Returns a string representation of the participant object, including the participant's name.
    """

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey("eventos.id"), nullable=False)

    def __repr__(self):
        return f"<Participante {self.nome}>"


class Eventos(db.Model):
    """
    Eventos Model
    Represents an event in the system.
    Attributes:
        id (int): The unique identifier for the event. Auto-incremented primary key.
        nome (str): The name of the event. Cannot be null and has a maximum length of 50 characters.
        data (datetime.date): The date of the event. Cannot be null.
        tema (str): The theme of the event. Cannot be null and has a maximum length of 40 characters.
        descricao (str): A description of the event. Cannot be null and has a maximum length of 200 characters.
        participantes (list): A relationship to the Participantes model, representing the participants of the event.
            This relationship is lazy-loaded and cascades all operations, including deletion of orphaned participants.
    Methods:
        __repr__(): Returns a string representation of the event, including its name.
    """

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
    """
    Represents a user in the system.
    Attributes:
        nickname (str): The unique identifier for the user, serving as the primary key.
        nome (str): The name of the user. This field is required.
        senha (str): The password of the user, stored as a hashed string. This field is required.
    Methods:
        __repr__(): Returns a string representation of the user object, displaying the user's name.
    """

    nickname = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
