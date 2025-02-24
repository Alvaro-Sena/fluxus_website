import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)

# Configurar sessao
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)  # Necessário para usar o flash
Session(app)

# Configurar SQLite
DATABASE = "fluxus.db"

import sqlite3

def db_execute(query, *params):
    """Executes the SQL query and returns results if it's a SELECT query"""
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        if query.lower().startswith('select'):
            return cursor.fetchall()
    except sqlite3.DatabaseError as e:
        flash(f"Database error: {e}", "error")
        return []
    finally:
        conn.close()


def create_tables():
    """Cria as tabelas necessárias no banco de dados"""
    db_execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        country TEXT NOT NULL,
        email TEXT NOT NULL
    );
    ''')

    db_execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        date_posted DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    ''')


# Chame essa função ao iniciar a aplicação
create_tables()


@app.route("/")
def index():
    """Exibe a página inicial"""
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    """Mostra sobre o site e permite que visitantes deixem comentários"""
    
    # Exibe os comentários
    try:
        comments = db_execute("SELECT c.message, c.date_posted, u.username FROM comments c JOIN users u ON c.user_id = u.id ORDER BY c.date_posted DESC")
    except Exception as e:
        flash(f"Error loading comments: {e}", "error")
        comments = []
    
    if request.method == "POST":
        message = request.form.get("message")
        if not message:
            flash("Please provide a message!", "error")
            return redirect("/about")

        # Armazenar o comentário no banco de dados
        db_execute("INSERT INTO comments (user_id, message, date_posted) VALUES (?, ?, ?)", session["user_id"], message, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        flash("Your comment has been posted!", "success")
        return redirect("/about")
    
    return render_template("about.html", comments=comments)


@app.route("/projects")
def projects():
    """Exibe uma página com os projetos do Fluxus"""
    return render_template("projects.html")


@app.route("/gallery")
def gallery():
    """Página para exibir uma galeria de fotos"""
    return render_template("gallery.html")


@app.route("/support")
def support():
    """Página de apoio ao site"""
    return render_template("support.html")


@app.route("/contact")
def contact():
    """Página para entrar em contato"""
    return render_template("contact.html")


# Funções de login e logout
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        # garante nome enviado
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # garante senha enviada
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # bd para username
        rows = db_execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # garante nome e senha corretos
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)


        session["user_id"] = rows[0]["id"]

        # Redireciona para home page
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Esquecer usuário
    session.clear()

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        country = request.form.get("country")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Verificando se os campos estão preenchidos
        if not username:
            return apology("must provide username", 400)
        if not full_name:
            return apology("must provide full name", 400)
        if not email:
            return apology("must provide email", 400)
        if not country:
            return apology("must provide country", 400)
        if not password:
            return apology("must provide password", 400)
        if not confirmation:
            return apology("must provide confirmation password", 400)
        if password != confirmation:
            return apology("passwords must match", 400)

        # Verificando se o nome de usuário já existe
        user_check = db_execute("SELECT * FROM users WHERE username = ?", username)
        if user_check:
            return apology("username already exists", 400)

        # Inserindo o novo usuário no banco de dados
        try:
            db_execute("INSERT INTO users (username, full_name, email, country, hash) VALUES (?, ?, ?, ?, ?)",
                       username, full_name, email, country, generate_password_hash(password))
        except sqlite3.IntegrityError:
            return apology("Error inserting user", 400)

        return redirect("/login")
    else:
        return render_template("register.html")


def apology(message, code=400):
    """Renderiza uma página de erro com a mensagem especificada"""
    return render_template("apology.html", message=message), code


@app.route("/check_username", methods=["POST"])
def check_username():
    username = request.json.get("username")  # Captura o nome de usuário a partir do JSON enviado
    if not username:
        return {"available": False, "message": "No username provided."}

    # Verifica no banco de dados se o nome de usuário já existe
    user_check = db_execute("SELECT * FROM users WHERE username = ?", username)
    if user_check:
        return {"available": False, "message": "Username already taken."}
    else:
        return {"available": True, "message": "Username available."}



if __name__ == "__main__":
    app.run(debug=True)
