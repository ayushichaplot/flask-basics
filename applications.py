from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ayushi")
def ayushi():
    return "Ayushi Chaplot"

@app.route("/<string:name>")
def helloo(name):
    name = name.capitalize()
    return f"<h1>Hello {name}</h1>"

@app.route("/headline")
def headline():
    headline = "World"
    return render_template("index.html", headline = headline)

@app.route("/list")
def list():
    names = ["Ayushi","Snehlata","Jerry","Tom"]
    return render_template("index.html", names = names)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
