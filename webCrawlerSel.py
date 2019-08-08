#----import----#
from pyquery import PyQuery as pq
from selenium import webdriver
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#--------------#
url = "https://www.imdb.com/"

#----使用url爬出需要的資料----#
def get_movie_info(movie_url):
    d = pq(movie_url)
    movie_rating = float(d("strong span").text())
    movie_genre = [x.text() for x in d(".subtext a").items()]
    movie_release_date = movie_genre.pop()
    movie_poster = d(".poster img").attr('src')
    movie_cast = [x.text() for x in d(".primary_photo+ td a").items()]

    # 電影資訊
    movie_info = {
        "movieRating": movie_rating,
        "movieReleaseDate": movie_release_date,
        "movieGenre": movie_genre,
        "moviePosterLink": movie_poster,
        "movieCast": movie_cast
    }
    return movie_info

#----自動化搜尋----#
def get_movies(*args):
    driver = webdriver.Chrome() 
    movies = dict()
    for movie_title in args:
        driver.get(url)
        # 搜尋欄位
        search = driver.find_element_by_xpath("//input[@id='navbar-query']")
        # 輸入電影名稱
        search.send_keys(movie_title)
        # 搜尋按鈕
        submit = driver.find_element_by_xpath("//div[@class='magnifyingglass navbarSprite']")
        # 點擊搜尋按鈕
        submit.click()
        # 篩選(movie)按鈕
        category = driver.find_element_by_xpath("//ul[@class='findTitleSubfilterList']/li[1]/a")
        # 點擊篩選(movie)按鈕
        category.click()
        # 搜尋結果連結
        first_result_elem = driver.find_element_by_xpath("//tr[@class='findResult odd'][1]/td[@class='result_text']/a")
        # 點擊搜尋結果連結
        first_result_elem.click()
        # 擷取當下的網址
        current_url = driver.current_url
        movie_info = get_movie_info(current_url)
        movies[movie_title] = movie_info
        time.sleep(3)
    driver.quit()
    return movies
#--------------#
result = get_movies("Avengers: Endgame", "Spider-Man: Far from Home")
print(result)