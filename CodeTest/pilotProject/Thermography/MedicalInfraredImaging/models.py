# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

from MedicalInfraredImaging import db
from datetime import datetime


# relationship table
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliNum = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(120))
    sex = db.Column(db.String(8))
    idNum = db.Column(db.String(18))
    phone = db.Column(db.String(11))
    addr = db.Column(db.String(240))
    images = db.relationship("UploadImage", back_populates="patient", cascade="all")
    records = db.relationship("MedRecord", back_populates="patient", cascade="all")
    clinicsOperator = db.relationship("InitClinic", back_populates="patient", cascade="all")
    clinicsDoc = db.relationship("DocClinic", back_populates="patient", cascade="all")


class UploadImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    description = db.Column(db.String(120))
    filename = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    patient = db.relationship("Patient", back_populates="images")


class MedRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    hisDescription = db.Column(db.String(500))
    lisDescription = db.Column(db.String(500))
    pacsDescription = db.Column(db.String(500))
    patient = db.relationship("Patient", back_populates="records")


class InitClinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    initClinic = db.Column(db.String(1500))
    patient = db.relationship("Patient", back_populates="clinicsOperator")


class DocClinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    docClinic = db.Column(db.String(1500))
    patient = db.relationship("Patient", back_populates="clinicsDoc")
