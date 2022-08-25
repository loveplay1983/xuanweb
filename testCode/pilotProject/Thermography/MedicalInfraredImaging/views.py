# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template
from MedicalInfraredImaging import app, db

@app.route("/")
def index():
    return render_template("index.html")