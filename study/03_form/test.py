# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""

import os
import uuid

from flask import Flask \
    , render_template \
    , flash \
    , redirect \
    , url_for \
    , request \
    , send_from_directory \
    , session

from flask_ckeditor import CKEditor, upload_success \
    , upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from forms import LoginForm, FortyTwoForm, NewPostForm, UploadForm, MultiUploadForm, SigninForm \
    , RegisterForm, SigninForm2, RegisterForm2, RichTextForm

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secret string")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Custom config
app.config["UPLOAD_PATH"] = os.path.join(app.root_path, "uploads")
if not os.path.exists(app.config["UPLOAD_PATH"]):
    os.makedirs(app.config["UPLOAD_PATH"])
app.config["ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif"]

# Flask config
# set request body's max length - 3MB
# app.config["MAX_CONTENT_LENGTH"]=3*1024*1024

# Flask-CKEditor config
app.config["CKEDITOR_SERVE_LOCAL"] = True
app.config["CKEDITOR_FILE_UPLOADER"] = "upload_for_ckeditor"

# Flask-Dropzone config
app.config["DROPZONE_ALLOWED_FILE_TYPE"] = "image"
app.config["DROPZONE_MAX_FILE_SIZE"] = 3  # 3MB - please check line 42
app.config["DROPZONE_MAX_FILES"] = 30

# Pass ckeditor and dropzone to flask instance
ckeditor = CKEditor(app)
dropzone = Dropzone(app)


# view functions
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/html", methods=["GET", "POST"])
def html():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        flash("Welcome home, {}".format(username))
        return redirect(url_for("index"))
    return render_template("pure_html.html")


@app.route("/basic", methods=["GET", "POST"])
def basic():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash("Welcome home, {}".form(username))
        return redirect(url_for("index"))
    return render_template("basic.html", form=form)

@app.route("/bootstrap", methods=["GET", "POST"])
def bootstrap():
    form=LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        flash("Welcome home, {}".form(username))
        return redirect(url_for("index"))
    return render_template("bootstrap.html", form=form)

@app.route()