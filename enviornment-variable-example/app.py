from flask import Flask, render_template
import os

app = Flask(__name__)

background_color = os.environ.get('BACKGROUND_COLOR')

@app.route("/")
def home():
    return render_template("home.html", color=background_color)