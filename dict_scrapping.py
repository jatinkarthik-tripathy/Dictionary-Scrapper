from bs4 import BeautifulSoup
import requests


def parser(url):
    sauce = requests.get(url)
    plaintxt = sauce.text
    soup = BeautifulSoup(plaintxt, 'html.parser')

    name = soup.find('h1', {'class':"hword"}).text
    print(name)

    pos = soup.find('div', {'class':'row entry-header'}).find('span').text
    print(pos)

    prounciation = soup.find('span', {'class':'pr'}).text
    print(prounciation)

    defi = soup.find('span', {'class':'dtText'}).text
    print(defi)




def run():
    url = 'https://www.merriam-webster.com/dictionary/eagle'
    parser(url)

if __name__ == '__main__':
    run()
