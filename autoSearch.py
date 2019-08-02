#----import----#
from selenium import webdriver
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#--------------#
url = "https://www.google.com/"
path = 'chromedriver'

#----自動化搜尋----#
def get_result(search_name):
    driver = webdriver.Chrome(path) 
    driver.get(url)
# 搜尋欄位
    search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
    #print("column check")
# 輸入搜尋關鍵字
    search.send_keys(search_name)
    #print("type check")
# 搜尋按鈕
    submit = driver.find_element_by_xpath("//div[@class='aajZCb']/div[@class='VlcLAe']/center/input[@class='gNO89b']")
    #print("search button check")
# 點擊搜尋按鈕
    time.sleep(3)
    submit.click()
    #print("click check 1")
# 選擇預設好的網頁
    link = driver.find_element_by_xpath("//a/h3[@class='LC20lb']")
    #print("link check")
# 點擊連結至網頁
    time.sleep(2)
    link.click()
    #print("click check 2")
# 擷取當下的網址
    current_url = driver.current_url
    print(current_url)

    time.sleep(3)
    driver.close()
    #print("close check")
    return "search success"
#--------------#
result = get_result("Ntub")
print(result)