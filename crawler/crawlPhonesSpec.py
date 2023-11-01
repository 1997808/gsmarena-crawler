import yaml
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup


def getPageContent(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')
