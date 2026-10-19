import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.basketball-reference.com/boxscores/pbp/202511020NYK.html'
response = requests.get(url)
html = response.text
print(html)
soup = BeautifulSoup(html, 'html.parser')

jump_ball_td = soup.find(lambda tag: tag.name == 'td' and "Jump ball" in tag.get_text())
#players = jump_ball_td.find_all("a")
player_links = jump_ball_td.find_all(lambda tag: tag.name == 'a')
for player in player_links:
    print(player.get_text(strip=True))
#print (player_links)

