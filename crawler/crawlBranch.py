import yaml
import requests
from bs4 import BeautifulSoup
import re
import os
import time



# 1. Get the branch page
def getBranchPage(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# 2. Get the branch list
def getBranchList(soup):
    BranchList = []

    # find table
    table = soup.find('table')

    # find all tr
    trs = table.find_all('tr')

    # find all td
    for tr in trs:
        tds = tr.find_all('td')
        for td in tds:
            BranchList.append(td)

    return BranchList

# 3. Parse the branch list
def parseBranchList(BranchList):
    BranchData = []
    defaultUrl = 'https://www.gsmarena.com/'
    for branch in BranchList:
        BranchUrl = defaultUrl+branch.find('a')['href']
        # BranchName = branch.find('a').text
        # Branch name and number of phone is separated by <br/>
        BranchName = branch.find('a').text.split('\n')[0]
        
        BranchData.append([BranchUrl, BranchName])

    return BranchData



if __name__ == '__main__':
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    soup = getBranchPage(config['BranchPageUrl'])
    # print(soup)
    BranchList = getBranchList(soup)
    # print(BranchList)
    BranchData = parseBranchList(BranchList)
    for branch in BranchData:
        print(branch)
    
