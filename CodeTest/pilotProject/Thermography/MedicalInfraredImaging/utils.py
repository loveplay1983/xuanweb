# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web
"""
from MedicalInfraredImaging import app
import os
import uuid


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename