# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask("MedicalInfraredImaging")
app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks=True
app.jinja_env.lstrip_blocks=True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from MedicalInfraredImaging import commands, errors, forms, models, views, settings