from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import time
import requests
driver = Chrome(r'C:/Projekty/webscraper/selenium/chromedriver.exe')






dict = {}
filtered_dict = {}
links_fixed = []
prices_fixed = []

wyszukiwanie_1 = input("Podaj co chcesz wyszukac 1.Spodnie 2.T-Shirt, Koszule, Bluzy, Swetry: ")
wyszukiwanie_2 = input("Podaj atrybuty przedmiotu ")
wyszukiwanie = wyszukiwanie_1 + " " + wyszukiwanie_2
cena = input("Podaj maksymalna cene: ")
strony = input("Podaj ilosc stron: ")

for x in range (1, int(strony)):
    #url = f"https://www.vinted.pl/ubrania?search_text=koszula&page{x}"
    driver.get(f'https://www.vinted.pl/ubrania?search_text={wyszukiwanie}&page{x}')

    print(f'https://www.vinted.pl/ubrania?search_text={wyszukiwanie}&page{x}')
    #page = requests.get(url).text
    #print(page)
    doc = BeautifulSoup(driver.page_source, "lxml")
    objects_section = doc.find(class_ = "feed-grid")
    links = objects_section.find_all(class_ = "ItemBox_overlay__1kNfX")
    prices = objects_section.find_all(class_ = "ItemBox_title-content__1LClm")

    for link in links:
        links_fixed.append(link.get('href'))
    for price in prices:
        prices_fixed.append(price.h3.string)


    for link, price in zip(links_fixed, prices_fixed):
        dict[link] = price

    for key in dict:
        s = dict[key]
        s = s[:-6]
        dict[key] = s


for key in dict:
    if(dict[key] != None and dict[key] != " "):
        if int(dict[key]) < int(cena) :
            filtered_dict[key] = dict[key]

for key in filtered_dict:
        print(key, '-->', filtered_dict[key])

with open("dane.txt", 'w') as f:
    for key in filtered_dict:
        txt = key
        print(txt)
        x = re.search(f"^.*{wyszukiwanie_1[:-1]}.*$", txt)
        if x:
            f.write(txt)
            f.write(" ")
            f.write(filtered_dict[key])
            f.write("\n")


