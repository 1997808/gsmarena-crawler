# import yaml
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service


# # Utility function
# def loadBrandsData(path, filename):
#     # load the brand data from csv
#     df = pd.read_csv(os.path.join(path, filename + ".csv"))
#     return df


# def createDriver():
#     # create the driver
#     service = Service('crawler\msedgedriver.exe')
#     service.start()
#     driver = webdriver.Remote(service.service_url)
#     return driver


# if __name__ == '__main__':
#     with open('crawler\config.yaml', 'r') as f:
#         config = yaml.safe_load(f)

#     Brands_data = loadBrandsData(
#         config['SavePath'], config['BrandsListFileName'])
