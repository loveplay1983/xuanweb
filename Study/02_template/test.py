# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""

import os
from flask import Flask \
    , render_template \
    , flash, redirect \
    , url_for, Markup \
    , flash

app = Flask(__name__)
app.secret_key =  os.getenv("SECRET_KEY", "secret string")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route("/watch")
def watchlist():
    return render_template('watchlistStatic.html', user=user, movies=movies)


@app.route("/")
def index():
    # return "jinja2 test"
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("range-slider-test.html")

@app.route("/flash")
def showFlash():
    flash(u"Hello, ths is flash!")
    # return redirect(url_for("index"))
    return "A"

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("errors/404.html"), 404