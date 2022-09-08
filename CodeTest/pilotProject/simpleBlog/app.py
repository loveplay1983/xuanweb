from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(app.root_path, "blog.db")
db = SQLAlchemy(app)


# model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


# view function
@app.route("/")
def index():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = BlogPost.query.filter_by(id=post_id).one()
    return render_template("post.html", post=post)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/addpost", methods=["POST"])
def addpost():
    title = request.form["title"]
    subtitle = request.form["subtitle"]
    author = request.form["author"]
    content = request.form["content"]

    post = BlogPost(title=title, subtitle=subtitle \
                    , author=author, content=content\
                    , date_posted=datetime.utcnow())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for("index"))

