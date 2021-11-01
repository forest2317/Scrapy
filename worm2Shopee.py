"""
Created on Fri Aug  6 15:31:39 2021
@author: 黃森林
爬虫shopee 購物網，擬以特定商品對不同的賣家作比價。
作成商品號、商品名稱、價格、賣家等資料表單。
主要以廻圈剖析至最終的鍵值。找出可利用的表單資料。
"""
import requests
import json
from bs4 import BeautifulSoup

headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
          Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/92.0.4515.107 Safari/537.36'}

url="https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword=ewelink\
    %E9%81%A0%E7%AB%AF%E9%96%8B%E9%97%9C&limit=60&newest=0&order=desc&page_type=\
        search&scenario=PAGE_GLOBAL_SEARCH&version=2"

page1=requests.get(url,headers=headers)
# page=json.loads(page1.text)#Ajax字串類型檔案轉變成
# python可應用字典檔案
src=json.loads(page1.text)
src=src['items']    #第一次以key找value
src1=src[:5]    #選定剖析範圍為前五家

print('item_basic' in src1) #Flase
listShopee=[]

for i in src1:
    dictdata= i['item_basic']   #第二次以key找value，以下第三次用遞迭方式以key找value
    listShopee.append({"商品代號":dictdata["itemid"],"賣家代號":dictdata["shopid"],\
        "物品名稱":dictdata["name"],"物品售價":dictdata["price"]})
for index,i in enumerate((listShopee)): #add index number at left of line
    print("*"*35,"選出第{}件商品及賣家".format(index+1),"*"*35)
    print(("物品名稱為:")+i['物品名稱'])
    print(("商品價格為:")+str((i['物品售價'])/100000)+"0元")
    print(("商品代號為:")+str(i['商品代號']))
    print(("賣家代號為:")+str(i['賣家代號']))
