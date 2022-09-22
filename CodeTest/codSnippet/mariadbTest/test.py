# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web 
"""
import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://xuan:pgjdcwn1983@127.0.0.1:3306/xuan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



# relationship table
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliNum = db.Column(db.Integer)
    name = db.Column(db.String(120))
    sex = db.Column(db.String(8))
    idNum = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    addr = db.Column(db.String(240))
    images = db.relationship("ImageData", back_populates="patient", cascade="all")
    records = db.relationship("MedRecord", back_populates="patient", cascade="all")
    clinics = db.relationship("ClinicData", back_populates="patient", cascade="all")


class ImageData(db.Model):
    id = db.Column( db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    filename = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    patient = db.relationship("Patient", back_populates="images")


class MedRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hisDescription = db.Column(db.String(500))
    lisDescription = db.Column(db.String(500))
    pacsDescription = db.Column(db.String(500))
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    patient = db.relationship("Patient", back_populates="records")


class ClinicData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    initClinic = db.Column(db.String(500))
    docClinic = db.Column(db.String(500))
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    patient = db.relationship("Patient", back_populates="clinics")
