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


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_imgs(url):
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue  # skip if img tag contains no src attr
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname):
    """
    Download the file with the given URL,
    and puts it in the folder followed by the pathname
    """
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    # Download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # Get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # Get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    # Progress bar, changing the unit to bytes instead of iteration,
    # Which is default by tqdm
    progress = tqdm(response.iter_content(1024), \
                    f"Downloading{filename}", \
                    total=file_size, \
                    unit="B", \
                    unit_scale=True, \
                    unit_divisor=1024)

    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def main(url, path):
    imgs = get_all_imgs(url)
    for img in imgs:
        download(img, path)






