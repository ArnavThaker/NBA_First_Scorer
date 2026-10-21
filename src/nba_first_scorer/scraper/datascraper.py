import requests
from bs4 import BeautifulSoup
import re

#TODO: Find a way to iterate over a team's list of box scores (found on main page for team). Start with Knicks.
url = 'https://www.basketball-reference.com/boxscores/pbp/202511020NYK.html'
response = requests.get(url)
response.encoding = 'UTF-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

jump_ball_td = soup.find(lambda tag: tag.name == 'td' and "Jump ball" in tag.get_text())
first_score_td = soup.find(lambda tag: tag.name == 'td' and "makes" in tag.get_text())

jump_ball_player_links = jump_ball_td.find_all(lambda tag: tag.name == 'a')
first_scorer_player_link = first_score_td.find(lambda tag: tag.name == 'a')
print(first_scorer_player_link)

players = list(map(lambda player: player.get_text(strip=True), jump_ball_player_links))
#print(players)

