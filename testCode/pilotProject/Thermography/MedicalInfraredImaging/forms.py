# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


# Data Collection
class PatientInfo(FlaskForm):
    patientNum = StringField("门诊号", validators=[DataRequired()])
    # patientName = StringField("姓名", render_kw={"readonly": True})
    patientName = StringField("姓名")
    patientSex = StringField("性别", validators=[Length(1)])
    patientID = StringField("身份证")
    patientPhone = StringField("电话")
    patientAddr = StringField("地址")
    patientSearch = SubmitField("检索", render_kw={"hidden": True})


class DataCollect(FlaskForm):
    pass


class InitialReport(FlaskForm):
    patientFirstClinic = TextAreaField()


# Clinical Form
class ClinicalInfo(FlaskForm):
    clinicNum = IntegerField("就诊号", validators=[DataRequired()])
    clinicName = StringField("姓名")
    clinicSex = StringField("性别", validators=[Length(1)])
    clinicID = IntegerField("身份证")
    clinicPhone = IntegerField("电话")
    clinicAddr = StringField("地址")
    clinicSearch = SubmitField("检索")


class DataDisplay(FlaskForm):
    pass


class FinalReport(FlaskForm):
    pass
