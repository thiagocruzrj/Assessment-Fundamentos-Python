import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import re

word = " ladies"


def count_once_word(soup, page):
  if (page.status_code == 200):
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
  return ([x for x in c if c.get(x) == 1])


def count_word(soup, page):
  if (page.status_code == 200):
    count = len(re.findall(word, soup.get_text()))
  return count


page = requests.get("http://brasil.pyladies.com/about")
soup = BeautifulSoup(page.content, 'html.parser')

print(count_once_word(soup, page))
print("Ocorrências da palavra ladies:", count_word(soup, page))