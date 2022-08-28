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


class PatientForm(FlaskForm):
    clinicNum = IntegerField("门诊号", validators=[DataRequired()])
    patientName = StringField("姓名")
    patientSex = StringField("性别", validators=[Length(1)])
    patientPhone = IntegerField("电话")
    patientAddr = StringField("地址")
    patientID = IntegerField("身份证")
