import requests
from bs4 import BeautifulSoup


def get_page_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    title = soup.title.string
    # print title
    return title
