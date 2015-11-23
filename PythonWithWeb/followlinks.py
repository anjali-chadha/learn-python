import urllib
from bs4 import *

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Rachael.html"
count = 7
position = 18

while(count > 0):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position - 1].get('href',None)
    print url 
    count -= 1