import sys
import yaml
import pandas as pd
import os
# import requests
# import random
from bs4 import BeautifulSoup
import time
# from crawlBranch import convertTime


from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


def createDriver():
    # create the driver
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    return webdriver.Edge(options=options)


def openURL(driver, url, idRecog, config) -> bool:
    wait = WebDriverWait(driver, config["DRIVER_WAIT_TIME"])
    try:
        driver.get(url)
    except:
        print("Cannot open url:", url)
        time.sleep(config['TIME_LOAD_PAGE'])
        return False

    try:
        wait.until(EC.presence_of_element_located(
            (By.ID, idRecog)))
    except:
        print("Cannot load page:", url)
        time.sleep(config['TIME_LOAD_PAGE'])
        return False

    time.sleep(config['TIME_LOAD_PAGE'])
    return True


# parse data from html to get phone specs
def parseDeviceData(soup) -> list:
    # get name
    try:
        Name = soup.find(
            'h1', class_='specs-phone-name-title').text
    except:
        Name = None

    # NETWORK section
    # get 5G bands
    try:
        if (soup.find('td', attrs={'data-spec': 'net5g'}).text):
            NETWORK_5G_bands = "Yes"
    except:
        NETWORK_5G_bands = "No"

    # LAUNCH section
    # get Announced
    try:
        LAUNCH_Announced = soup.find('td', attrs={'data-spec': 'year'}).text
    except:
        LAUNCH_Announced = None

    # get Resolution
    try:
        DISPLAY_Resolution = soup.find(
            'td', attrs={'data-spec': 'displayresolution'}).text
    except:
        DISPLAY_Resolution = None

    # get Chipset
    try:
        PLATFORM_Chipset = soup.find('td', attrs={'data-spec': 'chipset'}).text
    except:
        PLATFORM_Chipset = None

    # get CPU
    try:
        PLATFORM_CPU = soup.find('td', attrs={'data-spec': 'cpu'}).text
    except:
        PLATFORM_CPU = None

    # get GPU
    try:
        PLATFORM_GPU = soup.find('td', attrs={'data-spec': 'gpu'}).text
    except:
        PLATFORM_GPU = None

    # get Models
    try:
        MISC_Models = soup.find('td', attrs={'data-spec': 'models'}).text
    except:
        MISC_Models = None

    return [Name,
            NETWORK_5G_bands,
            LAUNCH_Announced,
            DISPLAY_Resolution,
            PLATFORM_Chipset,
            PLATFORM_CPU,
            PLATFORM_GPU,
            MISC_Models]


# Main function
# get all phone specs
def crawlAllPhoneSpecsMini(config, start=0, end=-1):
    # load all device url
    DeviceUrls = pd.read_csv(os.path.join(
        config['SavePath'], config['AllDevicesUrlsFileName'] + ".csv"))

    phoneSpecs = []
    print("Start crawling phone specs")
    startTime = time.time()

    # create webdriver
    driver = createDriver()

    # convert start and end to int
    try:
        start = int(start)
        if end == -1:
            end = len(DeviceUrls)
        else:
            end = int(end)
    except:
        print("Invalid start or end")
        return

    # get all phone specs
    for i in range(start, end):
        url = DeviceUrls['DeviceUrl'][i]
        print("\rCrawling device " + str(i+1) + ' ', end="")

        # try to open url
        if not openURL(driver, url, "specs-list", config):
            continue

        # get page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # parse data
        phoneSpecs.append([DeviceUrls['BrandName'][i],
                          url] + parseDeviceData(soup))

        # save data every 500 devices
        if (i+1) % config['SAVE_EVERY'] == 0:
            print(''.join(['\r', str(
                i+1-start), " devices crawled. Crawl time: ", convertTime(time.time() - startTime)]))

            savePhoneSpecs(config, phoneSpecs, temp=True)

    print()
    print("Total devices crawled:", len(phoneSpecs))
    print("Total time:", convertTime(time.time() - startTime))
    savePhoneSpecs(config, phoneSpecs, start, end)

    # close webdriver
    driver.close()


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


def savePhoneSpecs(config, phoneSpecs, start=0, end=-1, temp=False):
    columns = ['Brand', 'url', 'Name', 'NETWORK_5G_bands', 'LAUNCH_Announced', 'DISPLAY_Resolution', 'PLATFORM_Chipset', 'PLATFORM_CPU', 'PLATFORM_GPU',
               'MISC_Models']
    df = pd.DataFrame(phoneSpecs, columns=columns)

    if end == -1:
        end = len(df)

    if temp:
        df.to_csv(os.path.join(
            config['SavePath'], config['DevicesSpecsFileName'] + "_temp.csv"), index=False)
        return

    if start == 0 and end == -1:
        df.to_csv(os.path.join(
            config['SavePath'], config['DevicesSpecsFileName'] + ".csv"), index=False)
    else:
        df.to_csv(os.path.join(
            config['SavePath'], config['DevicesSpecsFileName'] + "_" + str(start) + "_" + str(end) + ".csv"), index=False)


if __name__ == "__main__":
    # load config
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlAllPhoneSpecsMini(config, start=12000, end=12002)
