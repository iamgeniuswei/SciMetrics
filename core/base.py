#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 11:33
# @Author  : Geniuswei
# @Email   : iamgeniuswei@sina.com
# @File    : base.py
# @Desc    : 定义作者、机构、关键词及其共现的基类

class CoOccurance(object):
    def __init__(self, key_a, key_b):
        self._key_a = key_a
        self._key_b = key_b
        self._occurance = 1

    def get_keys(self):
        return self._key_a + ';' + self._key_b

    def get_key_a(self):
        return self._key_a

    def get_key_b(self):
        return self._key_b

    def get_occurance(self):
        return self._occurance

    def add_occurance(self, increment:int):
        self._occurance += increment
