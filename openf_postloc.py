# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:48:10 2021
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
          Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/92.0.4515.107 Safari/537.36'}

url="https://www.post.gov.tw/post/internet/I_location/index_all.html"

page1=requests.get(url,headers=headers)
page1.encoding='utf-8'
soup.prettify()

@author: Forest Home

fp = open("postloc.txt", "w+", encoding='UTF-8')
fp.write(page1.text)
fp.close()
for i in range(1, 30, 9):
    for loc in postloc:
        # postloc=postloc.getText()
        loc=postloc[(i+3):(i+9)]
        print(loc)
    print(i)
"""

import requests
from bs4 import BeautifulSoup

page1=open('postloc.txt',encoding='UTF-8')
soup=BeautifulSoup(page1,"html.parser")
postloc=soup.select('table>tr>td') #自id="pointbluelineTitle"以下觀察
postOffice=[]

postName=soup.select('.rwd-close') #郵局名稱為class='rwd-close'
postname=[] #剖析取得郵局局名資料
for i in range(0,40):#擷取最大範圍
    loc=  postName[i*2] #跳開單數空行資料
    # print("第"+str(i)+"支局  " +loc.getText())
    postname.append(loc.string)
    
telpost=soup.find_all('td',{"headers":"ptel"})
postTel=[]  #剖析取得郵局電話資料
for i in range(0,40):#擷取最大範圍
    tel=  telpost[i*2] #跳開單數空行
    postTel.append(tel.string)

branchpost=soup.find_all('td',{"class":"detail2"})
postBranchSno=[]    #剖析取得郵局序列編號資料
for i in range(0,40):#擷取最大範圍
    Sno= branchpost[i*4-1]  #每四行有三筆空行資料，取第四筆資料內容
    postBranchSno.append(Sno.string)

addrpost=soup.find_all('td',{"class":"detail"})
postSite=[] #剖析取得郵局地址資料
for i in range(0,40):#擷取最大範圍
        #list has no gerText attribute, but element does
        postSite.append(addrpost[i].string) 
        
for i in range(0,40):#擷取最大範圍
        print('-'*40)
        print(postBranchSno[i],postname[i],postTel[i])
        print(postSite[i])

    #以下合併四種source成郵局完整資料 
zipdata= zip(postBranchSno,postname,postTel,postSite)
postOffice= list(zipdata)
print(postOffice)

