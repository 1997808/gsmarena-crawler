import yaml
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


# Utility function
def loadBrandsData(path, filename):
    # load the brand data from csv
    df = pd.read_csv(os.path.join(path, filename + ".csv"))
    return df


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


def saveAllDeviceUrlOfAllBrand(config, Devices_urls):
    df = pd.DataFrame(Devices_urls, columns=['BrandName', 'DeviceUrl'])
    df.to_csv(os.path.join(
        config['SavePath'], config['AllDevicesUrlsFileName'] + ".csv"), index=False)


# Selenium functions
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


def openURL(driver, url, idRecog, config):
    wait = WebDriverWait(driver, config["DRIVER_WAIT_TIME"])
    driver.get(url)
    try:
        wait.until(EC.presence_of_element_located(
            (By.ID, idRecog)))
    except TimeoutException as e:
        print("Wait Timed out")
        # print(e)
    except NoSuchElementException as ne:
        print("No such element")
        # print(ne)
    time.sleep(config['TIME_LOAD_PAGE'])


def findPhonesRow(driver):
    try:
        brand_link_rows = driver.find_element(
            By.CLASS_NAME, 'makers').find_elements(By.TAG_NAME, 'li')
    except TimeoutException as e:
        print("Wait Timed out")
        # print(e)
    except NoSuchElementException as ne:
        print("No such element")
        # print(ne)
    return brand_link_rows


def getPhonesLink(brand_link_rows, phones_link_list):
    for brand_link_row in brand_link_rows:
        phones_link_list.append(brand_link_row.find_element(
            By.TAG_NAME, 'a').get_attribute('href'))
    return phones_link_list


def goNextPage(driver, config):
    # scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # find the next page button
    try:
        # next_page = driver.find_element(By.CLASS_NAME, 'prevnextbutton')
        next_page = driver.find_element(By.XPATH, "//a[@title='Next page']")
    except TimeoutException as e:
        print("Wait Timed out")
        # print(e)
    except NoSuchElementException as ne:
        print("Only one page")
        # print(ne)
        return False

    time.sleep(config["TIME_CLICK"])

    # click the next page button
    try:
        next_page.click()
    except ElementClickInterceptedException as e:
        # print("Last page")
        return False

    return True


def crawlAllDeviceUrlOfABrand(driver, config, brand_url):
    # open the brand url
    openURL(driver, brand_url, 'wrapper', config)
    page = 1
    print("Page", page)

    # find the phones row
    brand_link_rows = findPhonesRow(driver)

    # get the phones link list
    phones_link_list = []
    phones_link_list = getPhonesLink(brand_link_rows, phones_link_list)

    # go to the next page
    while goNextPage(driver, config):
        page += 1
        print("Page", page)
        # find the phones row
        brand_link_rows = findPhonesRow(driver)

        # get the phones link list
        phones_link_list = getPhonesLink(brand_link_rows, phones_link_list)

        if page == config['MAX_PAGE']:
            break

    print("Total page:", page)
    return phones_link_list


def crawlAllDeviceUrlOfAllBrand(config, Brands_data):
    res = []
    BrandsName = Brands_data['BrandName']
    BrandUrls = Brands_data['BrandUrl']
    NumberOfPhones = Brands_data['NumberOfPhone']

    # create the driver
    driver = createDriver()

    # crawl all device url of all brand
    for i in range(len(Brands_data)):
        print(i+1, ". Brand", ": ", BrandsName[i], sep="")
        brand_url = BrandUrls[i]
        phones_link_list = crawlAllDeviceUrlOfABrand(
            driver, config, brand_url)

        if len(phones_link_list) == NumberOfPhones[i]:
            print("Number of links match with number of phones")
        else:
            print("Number of links not match with number of phones")
            print("Number of links:", len(phones_link_list))
            print("Number of phones:", NumberOfPhones[i])
        print()

        res.extend([[BrandsName[i], phone_link]
                   for phone_link in phones_link_list])

        # Test
        # break

    # close the driver
    driver.close()

    return res


# Main function
def crawlDevicesUrl(config):
    # load the brand data from csv
    Brands_data = loadBrandsData(
        config['SavePath'], config['BrandsListFileName'])

    print("Start crawling devices url")
    startTime = time.time()

    # crawl all device url of all brand
    Devices_urls = crawlAllDeviceUrlOfAllBrand(config, Brands_data)

    print("Finish crawling devices url")
    print("Crawling time:", convertTime(time.time() - startTime))

    # save all device url of all brand
    saveAllDeviceUrlOfAllBrand(config, Devices_urls)


if __name__ == "__main__":
    # load the config
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlDevicesUrl(config)
