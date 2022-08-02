# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""

import os
import uuid

from flask import Flask\
    , render_template\
    , flash\
    , redirect\
    , url_for\
    , request\
    , send_from_directory\
    , session

from flask_ckeditor import CKEditor, upload_success\
    , upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from forms import