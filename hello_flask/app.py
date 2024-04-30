from flask import Flask

app = Flask(__name__)


def bold(func):
    def inside_func():
        return "<b> " + func() + " </b>"

    return inside_func


def italic(func):
    def inside_func():
        return "<em> " + func() + " </em>"

    return inside_func


def underline(func):
    def inside_func():
        return "<u> " + func() + " </u>"

    return inside_func


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<img src='https://media.giphy.com/media/WYEWpk4lRPDq0/giphy.gif'>"

@app.route("/bye")
@bold
@italic
@underline
def bye():
    return "<h1>Bye!</h1>"

@app.route("/<name>")
def hello_user(name):
    return f"<h1>Hello {name}<h1>"

if __name__ == "__main__":
    app.run(debug=True)
