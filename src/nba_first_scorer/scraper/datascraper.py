import re

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.basketball-reference.com/boxscores/pbp/202511020NYK.html'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.find("td", class_="bbr-play-score")
jump_ball = soup.find_all('td', class_= 'center')
#jump_ball = soup.find('a', string=re.compile("possession"))
print(items)
print(jump_ball)

#for item in items:
#    print(item.text)

