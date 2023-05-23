from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>HELLO WORLD!!</p>"



@app.route("/goodbye")
def goodby_world():
    return "<h1>GOODBYE WORLD!!</p>"