# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request
from MedicalInfraredImaging import settings, db
from MedicalInfraredImaging.forms import Patient
from MedicalInfraredImaging.models import PatientData
from MedicalInfraredImaging.utils import *
import os


currentClinicNum = 0

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collect", methods=["GET", "POST"])
def collectData():
    patient = Patient()
    if patient.validate_on_submit():
        cliNum = patient.patientNum.data
        cliName = patient.patientName.data
        cliSex = patient.patientSex.data
        cliID = patient.patientID.data
        cliPhone = patient.patientPhone.data
        cliAddr = patient.patientAddr.data

        cliInfo = Patient(cliNum=cliNum, name=cliName, sex=cliSex,
                          idNum=cliID, phone=cliPhone, addr=cliAddr)
        db.session.add(cliInfo)
        db.session.commit()

    return render_template("collect.html", form=patient)



    #     pName = patient.patientName.data
    #     flash("欢迎就诊, {}!".format(pName))  # pName could be info[0]
    #
    #     saveDir = settings.UPLOAD_PATH
    #     if request.method == "POST":
    #         f = request.files.get("file")
    #         if f and allowed_file(f.filename):
    #             f.save(os.path.join(saveDir, f.filename))
    #
    # return render_template("collect.html", form=patient)

#
# @app.route("/dropImage", methods=["GET", "POST"])
# def dropImage():



# @app.route("/uploads/")
