from flask import Flask
import random

number = random.randint(0, 9)

app = Flask(__name__) 

# Main Route
@app.route("/")
def main_route():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

# Guess Route
@app.route("/<guess>")
def guess_route(guess):
    if int(guess) == number:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    elif int(guess) > number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    elif int(guess) < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"



if __name__ == "__main__": app.run(debug=True)