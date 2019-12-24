import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XfICLOhKiHt')
# print(page.status_code)
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# print(soup.find_all('img'))
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
# print(items[0])
# print(items[0].find(class_='period-name'))
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_name = []
short_desc = []
tempe = []

for item in items:
    period_name.append(item.find(class_='period-name').get_text())
    short_desc.append(item.find(class_='short-desc').get_text())
    tempe.append(item.find(class_='temp').get_text())

# print(short_desc)

weather = pd.DataFrame({
    'PERIOD': period_name,
    'SHORT DESCRIPTION': short_desc,
    'TEMPERATURE': tempe,
})

# print(weather)

weather.to_csv('weather.csv')
