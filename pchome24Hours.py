# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:36:20 2021

@author: Forest Home
"""

import requests
import json
from bs4 import BeautifulSoup
url="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=python&page=10&sort=sale/dc"

headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
          Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/92.0.4515.107 Safari/537.36'}

page1=requests.get(url,headers=headers)
product_no=0
data=json.loads(page1.text)
if 'prods' in data:
    products= data['prods']
    for product in products:
        product_no+=1
        print('第'+str(product_no)+"項： ", product['name'],product['price'])
