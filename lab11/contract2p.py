from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
hrefs = []
films_info = []

driver.get("https://megogo.net/ua/films");
links = [a for a in driver.find_elements(By.CSS_SELECTOR, ".thumb > a[href]")]

for link in links:
    hrefs.append(link.get_attribute('href'))

for href in hrefs:
    try:
        driver.get(href)
        imdb = driver.find_element(By.CSS_SELECTOR, ".videoInfoPanel-rating .value")
        converted_imdb = float(imdb.text.strip().replace(',',''))
        if(converted_imdb <= 8): continue
        film = driver.find_element(By.CLASS_NAME, "header-info-top")
        films_info.append(film.text)
    except ValueError:
        print(ValueError)


print(films_info)
