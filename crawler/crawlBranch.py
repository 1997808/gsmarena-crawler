import yaml
import requests
from bs4 import BeautifulSoup
import pandas as pd
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
        # parse branch data
        BranchUrl = defaultUrl+branch.find('a')['href']
        BranchName, NumberOfPhone = str(branch.find('a')).split("<br/>")
        BranchName = BranchName.split(">")[1]
        NumberOfPhone = int(NumberOfPhone.split(">")[1].split(" ")[0])

        BranchData.append([BranchName, NumberOfPhone, BranchUrl])

    return BranchData

# 4. Save the branch data
def saveBranchData(BranchData, path, filename):
    # save the branch data to csv
    df = pd.DataFrame(BranchData, columns=['BranchName', 'NumberOfPhone', 'BranchUrl'])
    df.to_csv(os.path.join(path, filename + ".csv"), index=False)

# 5. Main function
def crawlBranchData(config):
    startTime = time.time()

    soup = getBranchPage(config['BranchPageUrl'])
    BranchList = getBranchList(soup)
    BranchData = parseBranchList(BranchList)
    saveBranchData(BranchData, config['Path'], config['Filename'])

    endTime = time.time()
    enlapsedTime = endTime - startTime

# Util function
def convertTime(enlapsedTime):
    hours, rem = divmod(enlapsedTime, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)
    
    



if __name__ == '__main__':
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlBranchData(config['BranchData'])
    
