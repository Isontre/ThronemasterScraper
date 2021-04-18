from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Firefox(executable_path=r'geckodriver_win64/geckodriver.exe',options=options)


driver.get("http://game.thronemaster.net/?game=90001")

sleep(1) # This just works best
gameStateText = driver.find_element_by_id('gameStateText')
print(gameStateText.text)
winner = re.search(r"\n(\w*) ",gameStateText.text).group(1)

html = driver.page_source

soup = BeautifulSoup(html,features="html.parser")

winner = soup.find("div", {"id": "gameStateText"}).find('b').text.split(' ', 1)[0]

print(winner)