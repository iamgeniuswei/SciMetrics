#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 20:41
# @Author  : Geniuswei
# @Email   : iamgeniuswei@sina.com
# @File    : get_article_urllib.py
# @Desc    :
import urllib.request
from gne import GeneralNewsExtractor
from bs4 import BeautifulSoup
url = 'https://www.aqniu.com/learn/69720.html'
response = urllib.request.urlopen(url)
html = response.read()
# html = html.decode('utf-8')
attr1 = dict()
attr1['class'] = 'blog-title'
soup = BeautifulSoup(html, 'html.parser')
soup = soup.find('div', attrs={'class': 'blog-excerpt'})
print(soup)
title = soup.find('div', attrs={'class': 'blog-title'})
author = soup.find('span', attrs={'class': 'author'}).find('a')
date = soup.find('span', attrs={'class': 'date'})
print(title.getText())
print(author.getText())
print(date.getText())
