from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>HELLO WORLD!!</p>"

@app.route("/goodbye")
def goodby_world():
    return "<h1>GOODBYE WORLD!!</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"<h1>hello {name.title()}</h1>"

@app.route("/addition/<a>/<b>")
def addition(a,b):
    return f"<h1> {a} + {b} = {a+b}"