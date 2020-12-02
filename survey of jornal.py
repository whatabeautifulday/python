
import requests
import csv
import time
import numpy as np 
from bs4 import BeautifulSoup
## 使用假header
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#re = requests.get(url, headers=headers) 
#re.encoding = 'utf8'
#print(re.text)
#要搜尋的題目關鍵字&標題
q = 'signed+domination'
qq = 'https://scholar.google.com.tw/scholar?start=0&q='+ q +'&hl=zh-TW&as_sdt=0,5'
url = qq
items = list()
items2 = list()
for i in range(1): #往下爬3頁
    time.sleep(5)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("h3.gs_rt a") #topic
    journal = soup.select("div.gs_a")
    uu = soup.find(align="left")#下一頁後端網址
    #items = list()
    for u in uu :
        time.sleep(5)
        print ("本頁的URL為"+url)
        url = "https://scholar.google.com.tw"+ u["href"] #下一頁的網址
        for s in sel: #印出網址跟標題
            time.sleep(5)
            item = list()
            item.append(s.text)#把topic丟入item
            item.append(s["href"])#把link丟入item
            print(s.text)#TOPIC
            print(s["href"])#link
            #print(s["href"],s.text)
            items.append(item)
        for j in journal:
            item2 = list()
            item2.append(j.text)
            items2.append(item2)
            print(j.text)
A = np.array(items)
B = np.array(items2)
print(A)
print(B)
D = np.hstack((A, B))#items&items2左右合併
with open('TEST survey of signed domination.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('TOPIC', 'LINK','JOURNAL'))
    for item in items:
        writer.writerow((column for column in D))  


print(items)
print(items2)   
D = np.hstack((items, items2))
print(D)





