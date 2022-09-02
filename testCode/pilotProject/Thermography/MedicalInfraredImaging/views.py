# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request
from MedicalInfraredImaging import app, db
from MedicalInfraredImaging.forms import PatientInfo


@app.route("/", methods=["GET", "POST"])
def index():
    patientInfo = PatientInfo()
    if patientInfo.validate_on_submit() and request.method == "GET":
        return redirect(url_for("index"))
    patientInfo.patientNum.data = "000000"
    patientInfo.patientID.data = "330681198305201537"
    return render_template("index.html", form=patientInfo)
