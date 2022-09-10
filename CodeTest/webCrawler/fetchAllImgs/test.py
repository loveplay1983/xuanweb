# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

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
