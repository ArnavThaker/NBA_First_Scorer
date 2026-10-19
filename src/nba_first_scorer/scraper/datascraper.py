import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.basketball-reference.com/boxscores/pbp/202511020NYK.html'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

jump_ball_td = soup.find(lambda tag: tag.name == 'td' and "Jump ball" in tag.get_text())


print(jump_ball_td)

#for item in items:
#    print(item.text)

