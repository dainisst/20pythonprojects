import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ast.lv/lv/content/situacija-energosistema"
page = requests.get(url)
features = "html.parser"
soup = BeautifulSoup(page.text, features)

flow_div = soup.find_all('p')

print(flow_div)