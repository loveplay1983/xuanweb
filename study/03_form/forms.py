# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired\
    , FileAllowed
from wtforms import StringField, PasswordField, BooleanField\
    , IntegerField, TextAreaField,SubmitField, MultipleFileField\
from wtforms.validators import DataRequired, Length\
    , ValidationError, Email


# basic form example
class LoginForm(FlaskForm):
    username=StringField("Username", validators=[DataRequired])
    password=PasswordField("Password", validators=[DataRequired\
                                                   , Length(8, 128)])
    remember=BooleanField("Remember me")
    submit=SubmitField("Log in")



