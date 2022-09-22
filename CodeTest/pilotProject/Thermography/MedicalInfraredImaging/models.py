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
    cliNum = db.Column(db.Integer)
    name = db.Column(db.String(120))
    sex = db.Column(db.String(8))
    idNum = db.Column(db.Integer)
    phone = db.Column(db.String(11))
    addr = db.Column(db.String(240))
    images = db.relationship("ImageData", back_populates="patient", cascade="all")
    records = db.relationship("MedRecord", back_populates="patient", cascade="all")
    clinics = db.relationship("ClinicData", back_populates="patient", cascade="all")


class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
