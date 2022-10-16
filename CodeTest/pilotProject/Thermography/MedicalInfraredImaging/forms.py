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
    TextAreaField, SubmitField, MultipleFileField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, Email


# Data Collection
class PatientForm(FlaskForm):
    patientNum = StringField("门诊号", validators=[DataRequired()])
    patientName = StringField("姓名")
    patientSex = SelectField("性别", choices=[('男', '男'), ('女', '女')])
    patientID = StringField("身份证")
    patientPhone = StringField("电话")
    patientAddr = StringField("地址")
    image = MultipleFileField("影像上传", validators=[DataRequired()])
    clinic = CKEditorField("影像表现", validators=[DataRequired()])
    submit = SubmitField(label="上传")


class DocViewer(FlaskForm):
    pNum = StringField("门诊号", validators=[DataRequired()])
    pName = StringField("姓名", render_kw={"readonly": True})
    pSex = StringField("性别", render_kw={"readonly": True})
    pid = StringField("身份证", render_kw={"readonly": True})
    pPhone = StringField("电话", render_kw={"readonly": True})
    pAddr = StringField("地址", render_kw={"readonly": True})
    initClinic = TextAreaField(label="影像表现", render_kw={"readonly": True})
    submit = SubmitField(render_kw={"hidden": True})


class DocDecision(FlaskForm):
    pNum = StringField("请输入门诊号", validators=[DataRequired()])
    pClinic = CKEditorField("诊断建议", validators=[DataRequired()])
    submit = SubmitField(label="保存诊断")
