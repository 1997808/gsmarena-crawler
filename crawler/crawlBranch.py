import yaml
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time



# 1. Get the brand page
def getBrandsPage(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# 2. Get the brand list
def getBrandsList(soup):
    BrandsList = []

    # find table
    table = soup.find('table')

    # find all tr
    trs = table.find_all('tr')

    # find all td
    for tr in trs:
        tds = tr.find_all('td')
        for td in tds:
            BrandsList.append(td)

    return BrandsList

# 3. Parse the brand list
def parseBrandsList(BrandsList):
    BrandsData = []
    defaultUrl = 'https://www.gsmarena.com/'
    for brand in BrandsList:
        # parse brand data
        BrandUrl = defaultUrl+brand.find('a')['href']
        BrandName, NumberOfPhone = str(brand.find('a')).split("<br/>")
        BrandName = BrandName.split(">")[1]
        NumberOfPhone = int(NumberOfPhone.split(">")[1].split(" ")[0])

        BrandsData.append([BrandName, NumberOfPhone, BrandUrl])

    return BrandsData

# 4. Save the brand data
def saveBrandsData(BrandsData, path, filename):
    # save the brand data to csv
    df = pd.DataFrame(BrandsData, columns=['BrandName', 'NumberOfPhone', 'BrandUrl'])
    df.to_csv(os.path.join(path, filename + ".csv"), index=False)

# 5. Main function
def crawlBrandsData(config):
    print("Start crawling brand data...")
    startTime = time.time()

    soup = getBrandsPage(config['BrandsPageUrl'])
    BrandsList = getBrandsList(soup)
    BrandsData = parseBrandsList(BrandsList)
    saveBrandsData(BrandsData, config['SavePath'], config['BrandsListFileName'])

    endTime = time.time()
    enlapsedTime = endTime - startTime
    print("Finish crawling brand data...")
    print("Crawling time: {}".format(convertTime(enlapsedTime)))

# Util function
def convertTime(enlapsedTime):
    hours, rem = divmod(enlapsedTime, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours > 0:
        if minutes > 0:
            return "{:0>2} hours {:0>2} minutes {:05.2f} seconds".format(int(hours), int(minutes), seconds)
        else:
            return "{:0>2} hours {:05.2f} seconds".format(int(hours), seconds)
    elif minutes > 0:
        return "{:0>2} minutes {:05.2f} seconds".format(int(minutes), seconds)
    else:
        return "{:05.2f} seconds".format(seconds)
    
    



if __name__ == '__main__':
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlBrandsData(config)
    
