import click
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Flask!</h1>"

@app.cli.command()
def hello():
    # click - command line interface creation kit
    click.echo("Hello, world!")