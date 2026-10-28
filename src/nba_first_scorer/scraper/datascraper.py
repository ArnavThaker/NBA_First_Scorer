import requests
import re
from bs4 import BeautifulSoup
from src.nba_first_scorer.constants import constants

#TODO: Categorize URLs as home or away (given by string in front of .html)
#TODO: Attempt scraping every game for a team's home games to gather the relevant players (jump ball, possession, and scorer)
#TODO: Organize code and make it functional. Should a data scraper be a class? Probably not right?

nyk_url = constants.BASE_URL + constants.TEAMS_PATH + constants.LOGOS[19] + constants.GAMES_HTML_PATH
print(nyk_url)
response = requests.get(nyk_url)
response.encoding = 'UTF-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
all_box_scores = soup.find_all("td", attrs={'data-stat':'box_score_text'})
for link in all_box_scores:
    paths = link.a['href'].split("/")
    paths[0] = constants.BASE_URL
    paths.insert(2, constants.PLAY_BY_PLAY_PATH)
    print(paths)
    game_url = "/".join(paths)
    print(game_url)





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


