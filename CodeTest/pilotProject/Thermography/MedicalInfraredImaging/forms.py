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
class PatientForm(FlaskForm):
    patientNum = StringField("门诊号", validators=[DataRequired()])
    patientName = StringField("姓名")
    patientSex = StringField("性别")
    patientID = StringField("身份证")
    patientPhone = StringField("电话")
    patientAddr = StringField("地址")
    image = MultipleFileField("影像上传", validators=[DataRequired()])
    clinic = CKEditorField("初次评估", validators=[DataRequired()])
    submit = SubmitField(label="上传")


class DocViewer(FlaskForm):
    pNum = StringField("门诊号", validators=[DataRequired()])
    pName = StringField("姓名")
    pSex = StringField("性别")
    pid = StringField("身份证")
    pPhone = StringField("电话")
    pAddr = StringField("地址")
    submit1 = SubmitField(render_kw={"hidden": True})


class DocDecision(FlaskForm):
    pClinic = CKEditorField("影像评估", validators=[DataRequired()])
    submit2 = SubmitField(label="保存诊断")
