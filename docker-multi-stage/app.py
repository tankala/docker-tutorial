from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/<int(signed=True):number>")
def get_random_number(number):
    if number >= 0:
        random_number = randint(0, number)
        return f"Random number between 0 and {number}: {random_number}"
    else:
        random_number = randint(number, 0)
        return f"Random number between {number} and 0: {random_number}"