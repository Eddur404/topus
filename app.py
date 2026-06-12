from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user
)
from models import Usuario
from db import db
import hashlib
import os

app = Flask(__name__)

# Configurações
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "JWT")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicialização
db.init_app(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"


def hash_password(txt):
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()


@lm.user_loader
def user_loader(user_id):
    try:
        return Usuario.query.get(int(user_id))
    except Exception:
        return None


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("emailForm")
    senha = request.form.get("senhaForm")

    user = Usuario.query.filter_by(
        email=email,
        senha=hash_password(senha)
    ).first()

    if not user:
        return "Email ou senha incorretos", 401

    login_user(user)
    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "GET":
        return render_template("registrar.html")

    nome = request.form.get("nomeForm")
    email = request.form.get("emailForm")
    senha = request.form.get("senhaForm")

    usuario_existente = Usuario.query.filter_by(email=email).first()

    if usuario_existente:
        return "Este email já está cadastrado.", 400

    novo_user = Usuario(
        nome=nome,
        email=email,
        senha=hash_password(senha)
    )

    db.session.add(novo_user)
    db.session.commit()

    login_user(novo_user)

    return redirect(url_for("home"))


# Cria tabelas
with app.app_context():
    db.create_all()


# Apenas para execução local
if __name__ == "__main__":
    app.run(debug=True)