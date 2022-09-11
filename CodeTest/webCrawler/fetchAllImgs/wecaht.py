# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com

Comment: Note wechat has particular tag for image resource which is data-src
"""
# coding:utf-8
# __auth__ = "maiz"
# __date__ = "2021/3/27"
# import os
import requests
from bs4 import BeautifulSoup
import datetime
import os

# url = input("请输入url：")
# url = 'https://mp.weixin.qq.com/s?__biz=MzI4MzAxNzU3MA==&mid=2649159629&idx=1&sn=d63d2571aa1c0c9ca14fefd1f15047be&chksm=f3837fc0c4f4f6d62ed8c6af4a09f54af73182a9938f9ad984baf1ebc1fdf84df48d2c10fc73&mpshare=1&scene=23&srcid=0908T3nevW54iSbofXamKa2O&sharer_sharetime=1662609088930&sharer_shareid=6d5eaf21850267bfd7c8759114122690&exportkey=ASYoc44SifIXnFBhUTe2bm4%3D&acctmode=0'  # 获取连接
url = "https://unsplash.com/s/photos/japanese-girl"
curr_time = datetime.datetime.now()  # 获取系统时间
print(curr_time)  # 打印时间 测试用
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}  # 'cookie': 'tvfe_boss_uuid=4427f26b6d83d5d7; pgv_pvid=8192465356; pgv_pvi=2750494720; RK=cfw14pvSFY; ptcz=026939cd8bdd917551be81f3d0d2563bdb9e2d0805f4c83de8df0ea6af457e49; eas_sid=i1e690x1l8v2I68559J4e8K995; LW_sid=W1C6S0u1y8a2A6E864o8L480Z0; LW_uid=51H6V041L8i2n6Q8M4S8e4k0D0; uin_cookie=o0878530130; ied_qq=o0878530130; o_cookie=878530130; pac_uid=1_878530130; luin=o0878530130; lskey=000100000f95a236a0b3f6a309a1f6e4809612024104f9a476a9b0803995ce53ec225971d5d95f3164c7df7a; rewardsn=; wxtokenkey=777'}
path = datetime.datetime.strftime(curr_time, '%Y%m%d%H%M')  # 将时间格式化为字符生成时间戳到时候给文件夹命名用
print(path)
if os.path.exists(path):  # 检查是否存在这个文件夹
    print("属于这个时间点的文件夹已经创建好")
else:
    os.mkdir(path)  # 不存在则创建
    print("创建成功！！！！正在保存图片")
dirname = os.getcwd() + "/" + path  # 获取当前工作目录并加上之前的时间生成文件夹路径
req = requests.get(url=url, headers=headers).content.decode()  # 向刚才输入的公众号链接里面发送请求
# soup = BeautifulSoup(req, 'lxml')  # 用BeautifulSoup解析网页
soup = BeautifulSoup(req, 'html.parser')
res = soup.select('img')  # 获取该网页中所有的图片标签
a = 0
for i in res:  # 遍历所有的图片标签
    if i.get("data-src") == None:  # 如果这个标签内的data-src等于空的时候直接跳过
        pass
    else:  # 否则获取data-src里面的内容获取图片链接
        print(f'链接：{i.get("data-src")}类型为：{i.get("data-type")}')
    try:  # 尝试去保存图片 如果保存图片错误则抛出异常
        print(os.path.join(dirname, f'{a}.{i.get("data-type")}'))
        with open(os.path.join(dirname, f'{a}.{i.get("data-type")}'),
                  'wb') as f:  # 拼接路径+a.jpg a是等于数字 每添加一个 a自增一 相当于是给图片命名 并且以二进制的形式写入
            f.write(requests.get(url=i.get("data-src"), headers=headers).content)  # 向这个图片发送请求 并将图片的二进制写入
            f.close()  # 关闭写入
            a = a + 1  # a自增一
    except Exception as e:  # 抛出异常 增加程序强壮性
        print("该链接为空自动跳过！")
print(f"此次一共成功保存图片{a}张")
