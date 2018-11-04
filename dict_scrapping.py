from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
from word_class import word_details
import io

words = []
words_objs = []

def word_gen(words):
    letters = string.ascii_lowercase[0:]
    print(letters)

    driver = webdriver.Chrome('chromedriver.exe')
    url = 'http://www.randomwordgenerator.com/'
    driver.get(url)

    for letter in letters:
        num = driver.find_element_by_xpath('//*[@id="qty"]')
        num.clear()
        num.send_keys('4')

        first_let = driver.find_element_by_xpath('//*[@id="first_letter"]')
        first_let.clear()
        first_let.send_keys(letter)

        driver.find_element_by_xpath('//*[@id="options"]/table/tbody/tr[6]/td/input[2]').submit()

        plaintxt = driver.page_source
        soup = BeautifulSoup(plaintxt, 'html.parser')

        for word in soup.findAll('span', {'class':'support'}):
            words.append(word.text)

    print(words)
    driver.close()

def parser(url, words_objs):
    sauce = requests.get(url)
    plaintxt = sauce.text
    soup = BeautifulSoup(plaintxt, 'html.parser')

    name = soup.find('h1', {'class':"hword"}).text
    print(name)

    pos = soup.find('div', {'class':'row entry-header'}).find('span').text
    # print(pos)

    prounciation = soup.find('span', {'class':'pr'}).text
    # print(prounciation)

    defi = soup.find('span', {'class':'dtText'}).text
    # print(defi)

    wrd = word_details(name, pos, prounciation, defi)
    words_objs.append(wrd)


def run():
    word_gen(words)
    for word in words:
        url = 'https://www.merriam-webster.com/dictionary/' + word
        parser(url, words_objs)

    with io.open("DB.txt", "w+", encoding='utf8') as f:
        for word in words_objs:
            f.write(word.word)
            f.write("\n")
            f.write(word.pos)
            f.writelines("\n")
            f.write(word.prounciation)
            f.write("\n")
            f.write(word.defi)
            f.write("\n")
            f.write("\n")

if __name__ == '__main__':
    run()
