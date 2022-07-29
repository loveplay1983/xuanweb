import click
from flask import Flask\
    , request\
    , redirect\
    , url_for\
    , abort\
    , make_response\
    , json\
    , jsonify\
    , session\


app = Flask(__name__)

# index
# @app.route("/")
# def index():
#     return "<h1>This is Flask!</h1>"

# click test
@app.cli.command()
def clickTest():
    # click - command line interface creation kit
    click.echo("This is click test!")

# hello
@app.route("/")
@app.route("/hello")
def hello():
    # name = request.args.get("name", "Flask")  # get(key, default)
    # return "<h1>Hello, {}!</h1>".format(name)
    name = request.args.get("name")
    if name is None:
        name = request.cookies.get("name", "Xuan")
        response = "<h1>Hello, {}!".format(name)
        if "logged_in" in session:
            response += "[Authenticated]"
        else:
            response += "[Not Authenticated]"
        return response



# HTTP
@app.route("/httpTest", methods=["GET", "POST"])
def httpTest():
    return "<h1>Hello, HTTP!</h1>"

# URL manipulation
@app.route("/goback/<int:year>")
def goBack(year):
    return "<p>Welcome to {}!".format(2018 - year)

# redirect
@app.route("/tobaidu")
def baidu():
    # return redirect(url_for("hello"))
    return redirect("https://www.baidu.com")

# error code response
@app.route("/404")
def notFound():
    abort(404)

# return response with different formats
@app.route("/note", defaults={"content_type": "text"})
@app.route("/note/<content_type>")
def note(content_type):
    content_type = content_type.lower()
    if content_type == "text":
        body = """ This is plain text!"""
        response = make_response(body)
        response.mimetype = "text/plain"
    elif content_type == "html":
        body = """<!DOCTYPE html>
<html>
<head></head>
<body>
  <h1>Note</h1>
  <p>to: Peter</p>
  <p>from: Jane</p>
  <p>heading: Reminder</p>
  <p>body: <strong>Don't forget the party!</strong></p>
</body>
</html>
"""
        response = make_response(body)
        response.mimetype = "text/html"
    elif content_type == "xml":
        body = """<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Peter</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the party!</body>
</note>"""
        response = make_response(body)
        response.mimetype = "application/xml"
    elif content_type == "json":
        body = {"note":
            {
            "to" : "Peter",
            "from": "Xuan",
            "heading": "Party",
            "body": "Tonight, dont't forget it!"
            }
        }
        response = jsonify(body)
    else:
        abort(400)
    return response

# json-dumps(), load(), and json-jsonify
@app.route("/foo")
def foo():
    data = {
        "Name": "Xuan",
        "Gender": "Male"
    }

    response = make_response(json.dumps(data))
    response.mimetype = "application/json"
    return response

@app.route("/fooJsonify")
def fooJsonify():
    return jsonify(Name="Xuan", Age="39")
    # return jsonify({"Name": "Xuan", "Age": "39"})

# cookie
@app.route("/set/<a>")
def set_cookie(a):
    response = make_response(redirect(url_for("hello")))
    response.set_cookie("cookieTest", a)
    return response

# read cookie request object
# @app.route("/")
# @app.route("/hello")
# def hello():
#     name = request.args.get("name")
#     if name is None:
#         name = request.cookies.get("name", "Human")
#     return "<h1>Hello, {}".format(name)

# User loging simulation
@app.route("/login")
def login():
    session["logged_in"] = True
    return redirect(url_for("hello"))

import os
app.secret_key = os.getenv("SECRET_KEY", "secret string")
