# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

import re
import requests
from bs4 import BeautifulSoup

site = 'https://mp.weixin.qq.com/s?__biz=MzI4MzAxNzU3MA==&mid=2649159629&idx=1&sn=d63d2571aa1c0c9ca14fefd1f15047be&chksm=f3837fc0c4f4f6d62ed8c6af4a09f54af73182a9938f9ad984baf1ebc1fdf84df48d2c10fc73&mpshare=1&scene=23&srcid=0908T3nevW54iSbofXamKa2O&sharer_sharetime=1662609088930&sharer_shareid=6d5eaf21850267bfd7c8759114122690&exportkey=ASYoc44SifIXnFBhUTe2bm4%3D&acctmode=0&pass_ticket=F1o4eafe4bY8SF0hotyUe3eKTSVDAw4S%2FN5votkYq86euEru2QmSRsf2QVJ%2FvhHn&wx_header=0#rd&sourceChannelId=575221437'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['data-src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpeg|jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)