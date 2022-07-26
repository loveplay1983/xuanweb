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

path = "test"

url = "https://unsplash.com/s/photos/japanese-girl"

headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_imgs(url, headers):
    soup = bs(requests.get(url=url, headers=headers).content.decode(), "html.parser")
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


def main(path, url, headers):
    imgs = get_all_imgs(url=url, headers=headers)
    for img in imgs:
        download(img, pathname=path)


if __name__ == "__main__":
    main(path, url, headers)
