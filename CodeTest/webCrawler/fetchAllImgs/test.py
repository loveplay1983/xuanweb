# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

# from bs4 import *
# import requests
# import os
# def folder_create(images):
#     folder_name = input("Enter name of folder: ")
#     os.mkdir(folder_name)
#     download_images(images, folder_name)
# def download_images(images, folder_name):
#     count = 0
#     print(f"Found {len(images)} images")
#     if len(images) != 0:
#         for i, image in enumerate(images):
#             image_link = image["src"]
#             r = requests.get(image_link).content
#             with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
#                 f.write(r)
#                 count += 1
#         if count == len(images):
#             print("All the images have been downloaded!")
#         else:
#             print(f" {count} images have been downloaded out of {len(images)}")
# def main(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     images = soup.findAll('img')
#     folder_create(images)
# url = input("Enter site URL:")
# main(url)


# import urllib3
# from bs4 import BeautifulSoup
# page = urllib3.urlopen('http://www.youtube.com/')
# soup = BeautifulSoup(page)
# tags=soup.findAll('img')
# print "\n".join(set(tag['src'] for tag in tags))


import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

