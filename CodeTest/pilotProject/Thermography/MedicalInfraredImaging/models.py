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
    name = db.Column(db.String(50))
    sex = db.Column(db.String(2))
    idNum = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    addr = db.Column(db.String(100))
    images = db.relationship("Image", back_populates="patient", cascade="all")
    records = db.relationship("MedRecord", back_populates="patient", cascade="all")
    clinics = db.relationship("Clinic", back_populates="patient", cascade="all")


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
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


class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    initClinic = db.Column(db.String(500))
    docClinic = db.Column(db.String(500))
    patientID = db.Column(db.Integer, db.ForeignKey("patient.id"))
    patient = db.relationship("Patient", back_populates="clinics")
