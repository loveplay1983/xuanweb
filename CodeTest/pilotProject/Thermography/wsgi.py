# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web 
"""
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
