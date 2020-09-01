#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 20:41
# @Author  : Geniuswei
# @Email   : iamgeniuswei@sina.com
# @File    : get_article_urllib.py
# @Desc    :
import urllib.request
from gne import GeneralNewsExtractor
url = 'https://www.aqniu.com/learn/69720.html'
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode('utf-8')
extractor = GeneralNewsExtractor()
result = extractor.extract(html, noise_node_list=['//div[@class="comment-list"]'])
print(result)