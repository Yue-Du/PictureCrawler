# -*- coding: UTF-8 -*-
import requests        #导入requests包
from bs4 import BeautifulSoup
second_link = [] #存放二次链接图片号的集合
for page in range(3,4):
    url1 = 'https://www.zerochan.net/?p=' + str(page) #不同页的网站链接
    strhtml = requests.get(url1)  # Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#thumbs2 > li > a')
    for item in data:
        second_link.append(item.get('href'))

#print(second_link)

img_link = []
for num in second_link:
    url_2 = url1[:24] + num
    strhtml2 = requests.get(url_2)
    soup2=BeautifulSoup(strhtml2.text,'lxml')
    data2 = soup2.select('#large > a.preview')
    for item in data2:
        pic_link = item.get('href')
        img_link.append(item.get('href'))
    for num in range(len(img_link)):
        with open('cha'+str(num+1)+'.jpg', 'wb') as f:
            pic = requests.get(img_link[num])
            f.write(pic.content)



