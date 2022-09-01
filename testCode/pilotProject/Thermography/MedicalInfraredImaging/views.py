# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template
from MedicalInfraredImaging import app, db
from MedicalInfraredImaging.forms import PatientForm, ClinicForm


@app.route("/")
def index():
    patientForm = PatientForm()
    if patientForm.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("index.html", form=patientForm)
