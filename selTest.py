from selenium import webdriver
url = "https://www.google.com"
path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(url)