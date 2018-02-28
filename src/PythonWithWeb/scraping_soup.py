import urllib
from bs4 import BeautifulSoup
import re 

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_188474.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
    
print sum    