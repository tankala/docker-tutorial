from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "books.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

from models import Book

@app.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/create", methods=["POST"])
def create():
    book = Book(title=request.form.get("title"))
    db.session.add(book)
    db.session.commit()
    return redirect("/")

@app.route("/update", methods=["POST"])
def update():
    title = request.form.get("title")
    return render_template("update.html", title=title)

@app.route("/update-title", methods=["POST"])
def update_title():
    old_title = request.form.get("old_title")
    new_title = request.form.get("new_title")
    book = Book.query.filter_by(title=old_title).first()
    book.title = new_title
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")