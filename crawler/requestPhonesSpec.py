import random
import sys
import yaml
import pandas as pd
import os
import requests
# import random
from bs4 import BeautifulSoup
import time
# from crawlBranch import convertTime


# # get html from url
# def getPageContent(url):
#     r = requests.get(url)
#     return BeautifulSoup(r.text, 'html.parser')

def getPageContent(url):
    # Create a new requests session.
    session = requests.Session()

    # Set a random user agent.
    session.headers["User-Agent"] = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.80 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/98.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/604.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    ])

    # Add a random delay between requests.
    time.sleep(random.uniform(0, 1))

    # Make the request.
    response = session.get(url)

    # Check for a 429 error (Too Many Requests).
    if response.status_code == 429:
        # Wait for the number of seconds specified in the "Retry-After" header.
        retry_after = int(response.headers["Retry-After"])
        time.sleep(retry_after)
        print('Handle retry for url ' + url + ' ' + retry_after)

        # Retry the request.
        response = session.get(url)

    # If everything is successful, return the content of the page.
    if response.status_code == 200:
        # return response.content
        return BeautifulSoup(response.text, 'html.parser')
    else:
        # Raise an exception if the request failed.
        raise Exception(
            "Failed to get page content: {}".format(response.status_code))


# parse data from html to get phone specs
def parseDeviceData(soup) -> list:
    # get image url

    imgUrl = soup.select_one(
        'div', class_='specs-photo-main').select_one('img')['src']
    # get name

    Name = soup.select_one('h1', class_='specs-phone-name-title').text
    # NETWORK section
    # get technology

    NETWORK_Technology = soup.select_one(
        'a', attrs={'data-spec': 'nettech'}).text
    # get 2G bands

    NETWORK_2G_bands = soup.select_one('td', attrs={'data-spec': 'net2g'}).text
    # get 3G bands

    NETWORK_3G_bands = soup.select_one('td', attrs={'data-spec': 'net3g'}).text
    # get 4G bands

    NETWORK_4G_bands = soup.select_one('td', attrs={'data-spec': 'net4g'}).text
    # get 5G bands

    NETWORK_5G_bands = soup.select_one('td', attrs={'data-spec': 'net5g'}).text
    # get GPRS

    NETWORK_GPRS = soup.select_one('td', attrs={'data-spec': 'gprstext'}).text
    # get EDGE

    NETWORK_EDGE = soup.select_one('td', attrs={'data-spec': 'edge'}).text
    # get Speed

    NETWORK_Speed = soup.select_one('td', attrs={'data-spec': 'speed'}).text
    # LAUNCH section
    # get Announced

    LAUNCH_Announced = soup.select_one('td', attrs={'data-spec': 'year'}).text
    # get Status

    LAUNCH_Status = soup.select_one('td', attrs={'data-spec': 'status'}).text
    # BODY section
    # get Dimensions

    BODY_Dimensions = soup.select_one(
        'td', attrs={'data-spec': 'dimensions'}).text
    # get Weight

    BODY_Weight = soup.select_one('td', attrs={'data-spec': 'weight'}).text
    # get Build

    BODY_Build = soup.select_one('td', attrs={'data-spec': 'build'}).text
    # get SIM

    BODY_SIM = soup.select_one('td', attrs={'data-spec': 'sim'}).text
    # get IP Resistance

    BODY_OTHER = soup.select_one('td', attrs={'data-spec': 'bodyother'}).text
    # DISPLAY section
    # get Type

    DISPLAY_Type = soup.select_one(
        'td', attrs={'data-spec': 'displaytype'}).text
    # get Size

    DISPLAY_Size = soup.select_one(
        'td', attrs={'data-spec': 'displaysize'}).text
    # get Resolution

    DISPLAY_Resolution = soup.select_one(
        'td', attrs={'data-spec': 'displayresolution'}).text
    # get Protection

    DISPLAY_Protection = soup.select_one(
        'td', attrs={'data-spec': 'displayprotection'}).text
    # PLATFORM section
    # get OS

    PLATFORM_OS = soup.select_one('td', attrs={'data-spec': 'os'}).text
    # get Chipset

    PLATFORM_Chipset = soup.select_one(
        'td', attrs={'data-spec': 'chipset'}).text
    # get CPU

    PLATFORM_CPU = soup.select_one('td', attrs={'data-spec': 'cpu'}).text
    # get GPU

    PLATFORM_GPU = soup.select_one('td', attrs={'data-spec': 'gpu'}).text
    # MEMORY section
    # get Card slot

    MEMORY_Card_slot = soup.select_one(
        'td', attrs={'data-spec': 'memoryslot'}).text
    # get Internal

    MEMORY_Internal = soup.select_one(
        'td', attrs={'data-spec': 'internalmemory'}).text
    # MAIN CAMERA section
    # get cam 1 module type

    MAIN_CAM_1_Module = str(
        soup.select_one('td', attrs={'data-spec': 'cam1modules'}))
    if len(MAIN_CAM_1_Module) > 47:
        MAIN_CAM_1_Module = len(MAIN_CAM_1_Module.split('<br>'))
    else:
        MAIN_CAM_1_Module = 0
    # get cam 1 features

    MAIN_CAM_1_Features = soup.select_one(
        'td', attrs={'data-spec': 'cam1features'}).text
    # get cam 1 video

    MAIN_CAM_1_Video = soup.select_one(
        'td', attrs={'data-spec': 'cam1video'}).text
    # SELFIE CAMERA section
    # get cam 2 module type

    SELFIE_CAM_2_Module = str(
        soup.select_one('td', attrs={'data-spec': 'cam2modules'}))
    if len(SELFIE_CAM_2_Module) > 47:
        SELFIE_CAM_2_Module = len(SELFIE_CAM_2_Module.split('<br>'))
    else:
        SELFIE_CAM_2_Module = 0
    # get cam 2 features

    SELFIE_CAM_2_Features = soup.select_one(
        'td', attrs={'data-spec': 'cam2features'}).text
    # get cam 2 video

    SELFIE_CAM_2_Video = soup.select_one(
        'td', attrs={'data-spec': 'cam2video'}).text
    # SOUND section
    # get Loudspeaker

    SOUND_Loudspeaker = soup.select_one('a', attrs={'href': 'glossary.php3?term=loudspeaker'}).select_one_parent(
        'tr').select_one('td', class_='nfo').text
    # get 3.5mm jack

    SOUND_35mm_jack = soup.select_one('a', attrs={
        'href': 'glossary.php3?term=audio-jack'}).select_one_parent('tr').select_one('td', class_='nfo').text
    # COMMS section
    # get WLAN

    COMMS_WLAN = soup.select_one('td', attrs={'data-spec': 'wlan'}).text
    # get Bluetooth

    COMMS_Bluetooth = soup.select_one(
        'td', attrs={'data-spec': 'bluetooth'}).text
    # get GPS

    COMMS_GPS = soup.select_one('td', attrs={'data-spec': 'gps'}).text
    # get NFC

    COMMS_NFC = soup.select_one('td', attrs={'data-spec': 'nfc'}).text
    # get Radio

    COMMS_Radio = soup.select_one('td', attrs={'data-spec': 'radio'}).text
    # get USB

    COMMS_USB = soup.select_one('td', attrs={'data-spec': 'usb'}).text
    # FEATURES section
    # get Sensors

    FEATURES_Sensors = soup.select_one(
        'td', attrs={'data-spec': 'sensors'}).text
    # BATTERY section
    # get Type

    BATTERY_Type = soup.select_one(
        'td', attrs={'data-spec': 'batdescription1'}).text
    # get Stand by

    BATTERY_Stand_by = soup.select_one(
        'td', attrs={'data-spec': 'batstandby1'}).text
    # get Talk time

    BATTERY_Talk_time = soup.select_one(
        'td', attrs={'data-spec': 'battalktime1'}).text
    # get Music play

    BATTERY_Music_play = soup.select_one(
        'td', attrs={'data-spec': 'batmusicplayback1'}).text
    # MISC section
    # get Colors

    MISC_Colors = soup.select_one('td', attrs={'data-spec': 'colors'}).text
    # get SAR

    MISC_SAR = soup.select_one('td', attrs={'data-spec': 'sar-us'}).text
    # get SAR EU

    MISC_SAR_EU = soup.select_one('td', attrs={'data-spec': 'sar-eu'}).text
    # get Models

    MISC_Models = soup.select_one('td', attrs={'data-spec': 'models'}).text
    # get Price

    MISC_Price = soup.select_one('td', attrs={'data-spec': 'price'}).text
    return [imgUrl,
            Name,
            NETWORK_Technology,
            NETWORK_2G_bands,
            NETWORK_3G_bands,
            NETWORK_4G_bands,
            NETWORK_5G_bands,
            NETWORK_GPRS,
            NETWORK_EDGE,
            NETWORK_Speed,
            LAUNCH_Announced,
            LAUNCH_Status,
            BODY_Dimensions,
            BODY_Weight,
            BODY_Build,
            BODY_SIM,
            BODY_OTHER,
            DISPLAY_Type,
            DISPLAY_Size,
            DISPLAY_Resolution,
            DISPLAY_Protection,
            PLATFORM_OS,
            PLATFORM_Chipset,
            PLATFORM_CPU,
            PLATFORM_GPU,
            MEMORY_Card_slot,
            MEMORY_Internal,
            MAIN_CAM_1_Module,
            MAIN_CAM_1_Features,
            MAIN_CAM_1_Video,
            SELFIE_CAM_2_Module,
            SELFIE_CAM_2_Features,
            SELFIE_CAM_2_Video,
            SOUND_Loudspeaker,
            SOUND_35mm_jack,
            COMMS_WLAN,
            COMMS_Bluetooth,
            COMMS_GPS,
            COMMS_NFC,
            COMMS_Radio,
            COMMS_USB,
            FEATURES_Sensors,
            BATTERY_Type,
            BATTERY_Stand_by,
            BATTERY_Talk_time,
            BATTERY_Music_play,
            MISC_Colors,
            MISC_SAR,
            MISC_SAR_EU,
            MISC_Models,
            MISC_Price]


# Main function
# get all phone specs
def requestPhonesSpec(config, start=0, end=-1):
    # load all device url
    DeviceUrls = pd.read_csv(os.path.join(
        config['SavePath'], config['AllDevicesUrlsFileName'] + ".csv"))

    phoneSpecs = []
    print("Start crawling phone specs")
    startTime = time.time()

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
        try:
            soup = getPageContent(url)
            # parse data
            phoneSpecs.append([DeviceUrls['BrandName'][i],
                               url] + parseDeviceData(soup))
        except:
            continue

        # save data every 500 devices
        if (i+1) % config['SAVE_EVERY'] == 0:
            print(''.join(['\r', str(
                i+1-start), " devices crawled. Crawl time: ", convertTime(time.time() - startTime)]))

            savePhoneSpecs(config, phoneSpecs, temp=True)

    print()
    print("Total devices crawled:", len(phoneSpecs))
    print("Total time:", convertTime(time.time() - startTime))
    savePhoneSpecs(config, phoneSpecs, start, end)


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
    columns = ['Brand', 'url', 'imgUrl', 'Name', 'NETWORK_Technology', 'NETWORK_2G_bands', 'NETWORK_3G_bands', 'NETWORK_4G_bands', 'NETWORK_5G_bands', 'NETWORK_GPRS', 'NETWORK_EDGE', 'NETWORK_Speed', 'LAUNCH_Announced', 'LAUNCH_Status', 'BODY_Dimensions', 'BODY_Weight', 'BODY_Build', 'BODY_SIM', 'BODY_OTHER', 'DISPLAY_Type', 'DISPLAY_Size', 'DISPLAY_Resolution', 'DISPLAY_Protection', 'PLATFORM_OS', 'PLATFORM_Chipset', 'PLATFORM_CPU', 'PLATFORM_GPU', 'MEMORY_Card_slot',
               'MEMORY_Internal', 'MAIN_CAM_1_Module', 'MAIN_CAM_1_Features', 'MAIN_CAM_1_Video', 'SELFIE_CAM_2_Module', 'SELFIE_CAM_2_Features', 'SELFIE_CAM_2_Video', 'SOUND_Loudspeaker', 'SOUND_35mm_jack', 'COMMS_WLAN', 'COMMS_Bluetooth', 'COMMS_GPS', 'COMMS_NFC', 'COMMS_Radio', 'COMMS_USB', 'FEATURES_Sensors', 'BATTERY_Type', 'BATTERY_Stand_by', 'BATTERY_Talk_time', 'BATTERY_Music_play', 'MISC_Colors', 'MISC_SAR', 'MISC_SAR_EU', 'MISC_Models', 'MISC_Price']
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

    requestPhonesSpec(config, start=12000, end=12002)
