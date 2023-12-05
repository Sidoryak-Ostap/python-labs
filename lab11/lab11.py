from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
textes = []
words_list = []

def display_chart(dict_of_words):
    filtered_dict = {word: count for word, count in dict_of_words.items() if len(word) > 3}

    sorted_items = sorted(filtered_dict.items(), key=lambda x: x[1], reverse=True)
    top_10_words = dict(sorted_items[:10])

    words = list(top_10_words.keys())
    counts = list(top_10_words.values())    

    plt.xticks(rotation='vertical')
    plt.bar(words, counts)

    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.title('Word Counts')
    plt.show()


def format_link(y,m,d):
    if(m <= 9):
        return f"https://www.unian.ua/news/archive/{y}0{m}0{d}"
    else: 
        return f"https://www.unian.ua/news/archive/{y}{m}0{d}"

def process_info():
    new_data_list =  []

    for line in textes:
        line = line.lower().replace(',', '').replace('.','')
        new_data_list.append(line.split(' '))

    for words in new_data_list:
        for word in words:
            words_list.append(word)


def count_words():
    print(words_list)
    list_of_dict = {}
    for word in words_list:
        if word in list_of_dict:
            list_of_dict[word] += 1
        else:
            list_of_dict[word] = 1

    for word, count in list_of_dict.items():
        print(f"{word}: {count} times")
    return list_of_dict


def get_text_from_news(href):
    driver.get(href)
    text_elements = driver.find_elements(By.CSS_SELECTOR, ".article-text p")
    return text_elements
    

    # return text

def process_page_news():
    # search for a with href inside article with class "post"
    links = [a for a in driver.find_elements(By.CSS_SELECTOR, ".list-thumbs__image")]
    for link in links:
        href = link.get_attribute("href")
        text = get_text_from_news(href)
        for txt in text:
            textes.append(txt.text)
        driver.back()
        


for year in [2023]:
    for month in [1,2,3,4,5,6]:
        driver.get(format_link(year, month, 1))
        process_page_news()


driver.close()

process_info()
dic_of_words = count_words()
display_chart(dic_of_words)