#----import----#
from selenium import webdriver
import time
#--------------#
url = "https://www.google.com/"
driver = webdriver.Chrome() 
driver.get(url)
#----自動化搜尋----#
def get_result(search_name):
    driver.find_element_by_name("q").send_keys(search_name)
    submit = driver.find_element_by_name("btnK")
    time.sleep(3)
    submit.click()
    link = driver.find_element_by_xpath("//a/h3[@class='LC20lb']")
    time.sleep(2)
    link.click()
    #----搜尋結束----#
    time.sleep(5)
    driver.quit()
#--------------#
get_result("Ntub")