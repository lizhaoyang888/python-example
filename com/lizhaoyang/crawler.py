#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'lizhaoyang'

import requests

res = requests.get('https://www.baidu.com/')

print(res.text)