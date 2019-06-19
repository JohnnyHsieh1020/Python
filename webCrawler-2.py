#----import----#
import re
import urllib.request as req
import urllib.error as err
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#----function----#
def gethtmlfile(url):
    try:
        html = req.urlopen(url)
    except err.HTTPError as e:
        print(e)
        return None
    return html

def count(search):
    #----方法1----#
    total = html.count(search)
    #----方法2----#
    #count = re.findall(search, html)
    #print(count)
    #total = len(count)
    return total


#----主程式----#
request_url = 'http://invoice.etax.nat.gov.tw/'
htmlfile = gethtmlfile(request_url)
html = htmlfile.read().decode('utf-8')

if html != None:
    search = input("輸入你要搜尋的字 : ")
    if search in html:
        print("搜尋%s 成功" %(search))
    else:
        print("搜尋%s 失敗" %(search))
    total = count(search)

    if total != None:
        print("%s出現 %d 次" %(search, total))
    else:
        print("%s出現 0 次" %(search))
else:
    print("Web Load Fail!")