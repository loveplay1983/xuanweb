# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web
"""
from MedicalInfraredImaging import app

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
