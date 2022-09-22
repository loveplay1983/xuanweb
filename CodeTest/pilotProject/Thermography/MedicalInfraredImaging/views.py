# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request, send_from_directory
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from MedicalInfraredImaging import settings, db, app
from MedicalInfraredImaging.forms import PatientForm
from MedicalInfraredImaging.models import Patient, ImageData, ClinicData
from MedicalInfraredImaging.utils import allowed_file
import os

currentClinicNum = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collect", methods=["GET", "POST"])
def collectData():
    patient = PatientForm()
    if patient.validate_on_submit():

        # csrf check
        # try:
        #     validate_csrf(patient.csrf_token.data)
        # except ValidationError:
        #     flash("CSRF token error.")
        #     return redirect(url_for("collectData"))

        # Patient info
        cliNum = patient.patientNum.data
        cliName = patient.patientName.data
        cliSex = patient.patientSex.data
        cliID = patient.patientID.data
        cliPhone = patient.patientPhone.data
        cliAddr = patient.patientAddr.data
        cliInfo = Patient(cliNum=cliNum, name=cliName, sex=cliSex,
                          idNum=cliID, phone=cliPhone, addr=cliAddr)

        # image data
        # if "photo" not in request.files:
        #     flash("This field is required.")
        #     return redirect(url_for("collectData"))

        for f in request.files.getlist("image"):
            if f and allowed_file(f.filename):
                f.save(os.path.join(
                    app.config["UPLOAD_PATH"], f.filename
                ))
            else:
                flash("Invalid file type.")
                return redirect(url_for("collectData"))

        # Hand in the request to the database
        db.session.add(cliInfo)
        db.session.commit()

        return redirect(url_for("collectData"))
    return render_template("collect.html", form=patient)


@app.route("/uploads/<path:filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


# patient = PatientForm()
#     if patient.validate_on_submit():
#
#         # csrf check
#         # try:
#         #     validate_csrf(patient.csrf_token.data)
#         # except ValidationError:
#         #     flash("CSRF token error.")
#         #     return redirect(url_for("collectData"))
#
#         # Patient info
#         cliNum = patient.patientNum.data
#         cliName = patient.patientName.data
#         cliSex = patient.patientSex.data
#         cliID = patient.patientID.data
#         cliPhone = patient.patientPhone.data
#         cliAddr = patient.patientAddr.data
#         cliInfo = Patient(cliNum=cliNum, name=cliName, sex=cliSex,
#                           idNum=cliID, phone=cliPhone, addr=cliAddr)
#
#         # image data
#         # if "photo" not in request.files:
#         #     flash("This field is required.")
#         #     return redirect(url_for("collectData"))
#
#         for f in request.files.getlist("image"):
#             if f and allowed_file(f.filename):
#                 f.save(os.path.join(
#                     app.config["UPLOAD_PATH"], f.filename
#                 ))
#             else:
#                 flash("Invalid file type.")
#                 return redirect(url_for("collectData"))
#
#         # Hand in the request to the database
#         db.session.add(cliInfo)
#         db.session.commit()
#
#         return redirect(url_for("collectData"))
#     return render_template("collect.html", form=patient)