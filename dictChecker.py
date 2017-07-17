from bs4 import BeautifulSoup 
from urllib import request
import time 

word = input()
url = "http://www.ldoceonline.com/dictionary/" + word
content = request.urlopen(url).read()
soup = BeautifulSoup(content)

location = soup.find("span", class_="PRON").getText()

print('/', location, '/', sep='')
