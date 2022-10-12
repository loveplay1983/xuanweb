# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
import os
import sys
from MedicalInfraredImaging import app

dev_db = "mysql+pymysql://xuan:pgjdcwn1983@127.0.0.1:3306/thermography"
SECRET_KEY = os.getenv("SECRET_KEY", "secret string")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", dev_db)
DROPZONE_ALLOWED_FILE_TYPE = "image"
DROPZONE_MAX_FILE_SIZE = 10
DROPZONE_MAX_FILES = 30
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
UPLOAD_PATH = os.path.join(app.root_path, "uploads")
POST_PER_PAGE = 10