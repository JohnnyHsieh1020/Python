#連接網站
#import
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

src="https://www.ntub.edu.tw/"
with urllib.request.urlopen(src) as response:
    data=response.read().decode("utf-8")
print(data)
