#---- Web Crawler ----#
#----對象:PTT電影版的網頁
#find:只找一個
#find_all:找整個網頁

#----Import----#
import urllib.request as req
import bs4

#---- Start Web Crawler ----#
url = "https://www.ptt.cc/bbs/movie/index.html"
#----create an object called request, and add Headers's info----#
request = req.Request(url, headers = {
    "User-agent" : "Your user-agent"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8") # 網站原始碼(HTML)

#----使用Beautifulsoup解析HTML---#
root = bs4.BeautifulSoup(data, "html.parser")
articleTitle = root.find_all("div", class_ = "title") #找出 class="title" 的 div 標籤
print(root.title) #印出整個網頁的title
print(articleTitle) #印出找到的 class="title" 的 div 標籤

for title in articleTitle:
    if title.a != None: #若標題包含標籤 a , 印出來
        print(title.a.string)
#---- End Web Crawler ----#