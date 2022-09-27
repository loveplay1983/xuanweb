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
from MedicalInfraredImaging.forms import PatientForm, DocViewer
from MedicalInfraredImaging.models import Patient, UploadImage, MedRecord, InitClinic, DocClinic
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
        try:
            validate_csrf(patient.csrf_token.data)
        except ValidationError:
            flash("CSRF token error.")
            return redirect(url_for("collectData"))

        # Patient info
        cliNum = patient.patientNum.data
        cliName = patient.patientName.data
        cliSex = patient.patientSex.data
        cliID = patient.patientID.data
        cliPhone = patient.patientPhone.data
        cliAddr = patient.patientAddr.data
        cliInfo = Patient(cliNum=cliNum, name=cliName, sex=cliSex,
                          idNum=cliID, phone=cliPhone, addr=cliAddr)

        # Image data
        imageFiles = ","
        images = []
        for f in request.files.getlist("image"):
            if f and allowed_file(f.filename):
                destDir = os.path.join(app.config["UPLOAD_PATH"], cliNum)
                if not os.path.exists(destDir):
                    os.mkdir(destDir)
                f.save(os.path.join(destDir, f.filename))
                images.append(f.filename)
            else:
                flash("Invalid file type.")
                return redirect(url_for("collectData"))
        images = [str(each) for each in images]
        imageFiles = imageFiles.join(images)
        imageInfo = UploadImage(description=cliName, filename=imageFiles)
        cliInfo.images.append(imageInfo)

        # Clinic data
        clinicData = patient.clinic.data
        initClinic = InitClinic(initClinic=clinicData)
        cliInfo.clinicsOperator.append(initClinic)

        # Hand in the request to the database
        db.session.add(cliInfo)
        db.session.add(imageInfo)
        db.session.add(initClinic)
        db.session.commit()
        return redirect(url_for("collectData"))
    return render_template("collect.html", form=patient)


# @app.route("/uploads/<path:filename>")
# def get_file(filename):
#     return send_from_directory(app.config["UPLOAD_PATH"], filename)

@app.route("/clinic", methods=["GET", "POST"])
def clinicView():
    pView = DocViewer()
    return render_template("clinic.html", form=pView)

# @app.route("/clinic/viewer", method=["GET", "POST"])
# def