from bs4 import BeautifulSoup
from urllib import request
import time 

# url     = "https://weather.com/weather/today/l/CHXX0140:1:CH"
url = "http://www.weather.com.cn/weather/101230201.shtml"
content = request.urlopen(url).read()
soup = BeautifulSoup(content)

# location = soup.find("h1", class_="h4 today_nowcard-location").contents[0]
# tm = time.strftime('%X %Z')
# temperature = soup.find("div", class_="today_nowcard-temp").span.contents[0]
# temperature = int((int(temperature) - 32) * 5 / 9)
# feel_like = soup.find("span", class_="deg-feels").contents[0]
# feel_like = int((int(feel_like) - 32) * 5 / 9)

location = "        厦门天气"
tm = time.strftime("%X %Z")
temperature = soup.find_all("li", class_="on")[1].find("p", class_="tem").i.contents[0]
description = soup.find_all("li", class_="on")[1].find("p", class_="wea").contents[0]
highTemp = soup.find("ul", class_="t clearfix").find_all("li")[1].find("p", class_="tem").span.contents[0]
lowTemp = soup.find("ul", class_="t clearfix").find_all("li")[1].find("p", class_="tem").i.contents[0]
descrip2 = soup.find("ul", class_="t clearfix").find_all("li")[1].find("p", class_="wea").contents[0]
print()
print(location)
print("现在:    ", temperature, "   ", description)
print("明天:", highTemp, " /", lowTemp, " ", descrip2)
# print("feels like ", feel_like, '°C', sep='')
