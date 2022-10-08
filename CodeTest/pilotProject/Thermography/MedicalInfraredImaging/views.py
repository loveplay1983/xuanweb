# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request, send_from_directory, make_response
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from MedicalInfraredImaging import settings, db, app
from MedicalInfraredImaging.forms import PatientForm, DocViewer, DocDecision
from MedicalInfraredImaging.models import Patient, UploadImage, MedRecord, InitClinic, DocClinic
from MedicalInfraredImaging.utils import allowed_file
import os
# from MedicalInfraredImaging.utils import MyEncoder
# import json
# from MedicalInfraredImaging.utils import DuplicatedID

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
        try:
            db.session.add(cliInfo)
            db.session.add(imageInfo)
            db.session.add(initClinic)
            db.session.commit()
            return redirect(url_for("collectData"))
        # except Exception as e:
        #     e = {"异常名称": e}
        #     flash(json.dumps(e, cls=MyEncoder, indent=4))
        except Exception:
            return redirect(url_for("duplicatedPatientID"))
    return render_template("collect.html", form=patient)


@app.route("/uploads/<path:fileFolder>/<path:fileName>")
def getFile(fileFolder, fileName):
    return send_from_directory(os.path.join(app.config["UPLOAD_PATH"], fileFolder),
                               fileName)


@app.route("/clinic", methods=["GET", "POST"])
def clinicView():
    cliView = DocViewer()

    if cliView.validate_on_submit():
        patient = Patient.query.filter_by(cliNum=cliView.pNum.data).first()
        # csrf check
        try:
            validate_csrf(cliView.csrf_token.data)
        except ValidationError:
            flash("CSRF token error.")
            return redirect(url_for("clinicView"))

        if patient is not None:
            cliView.pNum.data = patient.cliNum
            cliView.pName.data = patient.name
            cliView.pSex.data = patient.sex
            cliView.pid.data = patient.idNum
            cliView.pPhone.data = patient.phone
            cliView.pAddr.data = patient.addr

            flash(f"就诊人员, {patient.name}!")

            # Test for retrieving the filenames
            fileFolder = cliView.pNum.data
            pid = Patient.query.filter_by(cliNum=cliView.pNum.data).first()
            img = UploadImage.query.filter_by(patientID=pid.id).first()
            imgs = img.filename.split(",")
            return render_template("clinic.html", form=cliView,
                                   fileFolder=fileFolder, files=imgs)
        else:
            flash(f"未找到相关人员!!!")
            return redirect(url_for("clinicView"))
    return render_template("clinic.html", form=cliView)


@app.route("/clinic/doc-write", methods=["GET", "POST"])
def docWrite():
    # flash("write test")
    form = DocDecision()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(cliNum=form.pNum.data).first()
        pid = patient.id
        docClinic = form.pClinic.data
        docText = DocClinic(patientID=pid, docClinic=docClinic)

        db.session.add(docText)
        db.session.commit()

        flash("a")
        return redirect(url_for("clinicView"))

    return render_template("docWrite.html", form=form)
