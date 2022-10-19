# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web
"""
from MedicalInfraredImaging import app
import os
import re
import uuid
import secrets
import json
import datetime


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            print("MyEncoder-datetime.datetime")
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        # elif isinstance(obj, array):
        #    return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


def removeTag(raw):
    cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(cleaner, "", raw)


def genSecretKey():
    # return os.urandom(12)
    # return secrets.token_urlsafe(16)
    # return secrets.token_bytes(12)
    # return secrets.token_hex(12)
    randKey = uuid.uuid4().hex
    with open(".env", "w") as env:
        env.write(f"SECRET_KEY={randKey}")
