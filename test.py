'''
https://www.benzinga.com/money/premarket-movers/
Shorts biggest premarket gainers, sell at 10:30/11 with a decent stoploss
Trailing stoplosses are not supported yet by Alpaca, so for now we will set the stoploss at the entry point
https://www.swaggystocks.com/dashboard/stocklabs/option-flow/TSLA
'''

from bs4 import BeautifulSoup, Comment
from selenium import webdriver
import time

url = 'https://www.benzinga.com/money/premarket-movers/'

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, features="lxml")
# remove comments
for element in soup(text=lambda text: isinstance(text, Comment)):
    element.extract()

gainers = [item.text for item in soup.find('div', {'id': 'stock-results'}).find('div', {'id': 'gainers'}).find_all('span', {'class': 'flex-item-result ticker'}) if item.text.isalpha()]
losers = [item.text for item in soup.find('div', {'id': 'stock-results'}).find('div', {'id': 'losers'}).find_all('span', {'class': 'flex-item-result ticker'}) if item.text.isalpha()]

'''
TODO:
- log initial gainers and losers list
- stream data. calculate trailing stop loss yourself.
'''