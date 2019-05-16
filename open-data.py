#公開資料的抓取
#import
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with urllib.request.urlopen(src) as response:
    data=json.load(response) #使用 json 模組處理資料
#Company list
clist=data["result"]["results"] #抓公司資料的列表
#print(clist)
with open("other file/data.txt", "w", encoding="utf-8")as file: #建立一個 data.txt 檔案
    for company in clist:
        file.write(company["公司名稱"]+"\n") #寫入檔案
