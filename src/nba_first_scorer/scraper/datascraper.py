import requests
from bs4 import BeautifulSoup
import re

#TODO: Find a way to construct links from the extracted href for a single team (again, starting with the Knicks). Will need to concatenate pbp to the strings and build off the base URL
url = 'https://www.basketball-reference.com/teams/NYK/2026_games.html'
response = requests.get(url)
response.encoding = 'UTF-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
all_box_scores = soup.find_all("td", attrs={'data-stat':'box_score_text'})
for link in all_box_scores:
    print(link.a['href'])





'''SAMPLE WORKING CODE AND EXAMPLE BELOW

url = 'https://www.basketball-reference.com/boxscores/pbp/202510220NYK.html'
response = requests.get(url)
response.encoding = 'UTF-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

jump_ball_td = soup.find(lambda tag: tag.name == 'td' and "Jump ball" in tag.get_text())
first_score_td = soup.find(lambda tag: tag.name == 'td' and "makes" in tag.get_text())




#Find the players at the jump ball and the winning
players = list(map(lambda player: player.get_text(strip=True), jump_ball_player_links))
print(players)

#Find the first scorer
jump_ball_player_links = jump_ball_td.find_all(lambda tag: tag.name == 'a')
first_scorer_player_link = first_score_td.find(lambda tag: tag.name == 'a')
print(first_scorer_player_link)
'''


