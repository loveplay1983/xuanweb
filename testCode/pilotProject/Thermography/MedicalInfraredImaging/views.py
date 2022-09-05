# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request
from MedicalInfraredImaging import app, db
from MedicalInfraredImaging.forms import PatientInfo


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collect", methods=["GET", "POST"])
def collectData():
    patientInfo = PatientInfo()
    if patientInfo.validate_on_submit():
        pName = patientInfo.patientName.data
        flash("欢迎就诊, {}!".format(pName))
    uname = request.form.get("patientNum")

    # To-Do
    """
    
    """

    return render_template("collect.html", form=patientInfo, uname=uname)
