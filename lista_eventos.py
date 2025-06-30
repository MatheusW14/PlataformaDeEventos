from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from helpers import recupera_imagem

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


@app.context_processor
def inject_helpers():
    return dict(recupera_imagem=recupera_imagem)


from views_eventos import *
from views_user import *

if __name__ == "__main__":
    app.run(debug=True)
