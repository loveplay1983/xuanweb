# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
from flask import flash, redirect, url_for, render_template, request
from flask_dropzone import Dropzone
from MedicalInfraredImaging import app, db
from MedicalInfraredImaging.forms import PatientInfo


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/collect", methods=["GET", "POST"])
def collectData():
    patientInfo = PatientInfo()      # PatientInfo - The first form class

    if patientInfo.validate_on_submit():
        pNum = request.form.get("patientNum")
        # To-Do
        # Raw SQL in via SQLALchemy
        # https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app
        """
        1. Retrieve user input pNum;
            ```
            pNum = request.form.get("patientNum")
            ```
        2. Query patient info includes name, sex, id, phone, and address, etc. 
           by pNum via db.engine.execute('xxx')
           ```
           info = db.engine.execute("SELECT name, sex, id, phone, addr FROM xxx WHERE p-num = pNum")
           ```
        3. Pass the query result back to the PatientInfo() form class, 
           and set each field with the corresponding result data 
           patientInfo.patientName.data = info[0]
           patientInfo.patientSex.data = info[1]
           patientInfo.patientID.data = info[2]
           patientInfo.patientPhone.data = info[3]
           patientInfo.patientAddr.data = info[4] 
        """
        pName = patientInfo.patientName.data
        flash("欢迎就诊, {}!".format(pName))  # pName could be info[0]
    return render_template("collect.html", form=patientInfo)


@app.route("/drop-upload", methods=["GET", "POST"])
def dropUpload():
    if request.method == "POST":
        if "file" not in request.files:


