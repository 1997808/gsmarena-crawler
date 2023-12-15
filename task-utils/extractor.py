import pandas as pd
import os
import numpy as np
import re




# DISPLAY SECTION

# DISPLAY_Type
def handleNull_Type(data: pd.DataFrame):
    # tim kiem va cap nhat bang ten dien thoai
    # Motorola V560
    data.loc[data['DISPLAY_Type'].isnull() & (data['Name'] == 'Motorola V560'), 'DISPLAY_Type'] = 'TFT'
    # Sendo S1
    data.loc[data['DISPLAY_Type'].isnull() & (data['Name'] == 'Sendo S1'), 'DISPLAY_Type'] = 'TFT'
    # Vertu Diamond
    data.loc[data['DISPLAY_Type'].isnull() & (data['Name'] == 'Vertu Diamond'), 'DISPLAY_Type'] = 'TFT'
    # Vertu Ascent
    data.loc[data['DISPLAY_Type'].isnull() & (data['Name'] == 'Vertu Ascent'), 'DISPLAY_Type'] = 'Graphical, TFD'

def unifyType(data: pd.DataFrame):
    # lowercase
    data['DISPLAY_Type'] = data['DISPLAY_Type'].str.lower()

    # TFT neu co chua các từ sau: 'tft'
    data.loc[data['DISPLAY_Type'].str.contains(
        'tft'), 'DISPLAY_Type'] = 'TFT'
    
    # TFD neu co chua các từ sau: 'tfd'
    data.loc[data['DISPLAY_Type'].str.contains(
        'tfd'), 'DISPLAY_Type'] = 'TFD'

    # IPS neu chua: ips
    data.loc[data['DISPLAY_Type'].str.contains(
        'ips') == True, 'DISPLAY_Type'] = 'IPS'
    
    # OLED neu chua: oled
    data.loc[data['DISPLAY_Type'].str.contains(
        'oled') == True, 'DISPLAY_Type'] = 'OLED'

    # CSTN neu chua: cstn
    data.loc[data['DISPLAY_Type'].str.contains(
        'cstn') == True, 'DISPLAY_Type'] = 'CSTN'
    
    # FSTN neu chua: fstn
    data.loc[data['DISPLAY_Type'].str.contains(
        'fstn') == True, 'DISPLAY_Type'] = 'FSTN'

    # STN neu chua: stn
    data.loc[data['DISPLAY_Type'].str.contains(
        'stn') == True, 'DISPLAY_Type'] = 'STN'

    # TN neu chua: tn
    data.loc[data['DISPLAY_Type'].str.contains(
        'tn') == True, 'DISPLAY_Type'] = 'TN'

    # PLS neu chua: pls
    data.loc[data['DISPLAY_Type'].str.contains(
        'pls') == True, 'DISPLAY_Type'] = 'PLS'
    
    # Alphanumeric neu chua: alphanumeric
    data.loc[data['DISPLAY_Type'].str.contains(
        'alphanumeric') == True, 'DISPLAY_Type'] = 'Alphanumeric'
    
    # Monochrome neu chua: monochrome
    data.loc[data['DISPLAY_Type'].str.contains(
        'monochrome') == True, 'DISPLAY_Type'] = 'Monochrome'

    # Grayscale neu chua: grayscale, greyscale
    data.loc[data['DISPLAY_Type'].str.contains(
        'grayscale|greyscale') == True, 'DISPLAY_Type'] = 'Grayscale'

    # Backlit neu chua: backlit
    data.loc[data['DISPLAY_Type'].str.contains(
        'backlit') == True, 'DISPLAY_Type'] = 'Backlit'
    
    # S-LCD neu chua: s-lcd, super lcd, super-lcd, superlcd
    data.loc[data['DISPLAY_Type'].str.contains(
        's-lcd|super lcd|super-lcd|superlcd') == True, 'DISPLAY_Type'] = 'S-LCD'
    
    # color neu chua: color
    data.loc[data['DISPLAY_Type'].str.contains(
        'color') == True, 'DISPLAY_Type'] = 'Color'
    
    # LCD neu chua: lcd, crystal,  mva, pureled
    data.loc[data['DISPLAY_Type'].str.contains(
        'lcd|crystal|mva|pureled') == True, 'DISPLAY_Type'] = 'LCD'
    
    # Con lai la 'Unknown'
    data['DISPLAY_Type'].replace([i for i in data['DISPLAY_Type'].unique() if i not in ['TFT', 'TFD', 'IPS', 'OLED', 'CSTN', 'FSTN', 'STN', 'TN', 'PLS', 'Alphanumeric', 'Monochrome', 'Grayscale', 'Backlit', 'S-LCD', 'Color', 'LCD']], 'Unknown', inplace=True)
        
def extract_display_type(data :pd.DataFrame, inplace :bool=False):
    if inplace == False:
        data = data.copy()
    
    handleNull_Type(data)
    unifyType(data) 
    return data


# DISPLAY_Size
def handleNull_Size(data: pd.DataFrame):
    # Nếu trong giá trị ko có 'inch' thì được coi là null
    data.replace([i for i in data['DISPLAY_Size'].unique() if 'inch' not in str(i)], np.nan, inplace=True)
    
    data['DISPLAY_Size'].fillna(data['DISPLAY_Size'].mode()[0], inplace=True)

def unifySize(data: pd.DataFrame):
    # Tach chuoi tai tu inch va lay phan truoc
    data['DISPLAY_Size'] = data['DISPLAY_Size'].str.split(' inch').str[0]

    # Chuyen ve dang float cho tung dong
    for i in range(len(data['DISPLAY_Size'])):
        try:
            data.loc[i, 'DISPLAY_Size'] = float(data.loc[i, 'DISPLAY_Size'])
        except:
            print(i, data.loc[i, 'DISPLAY_Size'])
    
    # Chuyen ve dang float cho toan bo cot
    try:
        data['DISPLAY_Size'] = data['DISPLAY_Size'].astype(float)
    except:
        print('Cannot convert to float')

def extract_display_size(data: pd.DataFrame, inplace: bool=False):
    if inplace == False:
        data = data.copy()
    
    handleNull_Size(data)
    unifySize(data)
    return data


# DISPLAY_Resolution
def extract_display_resolution(data: pd.DataFrame, inplace: bool=False):
    if inplace == False:
        data = data.copy()
    
    # drop DISPLAY_Resolution
    data.drop('DISPLAY_Resolution', axis=1, inplace=True)

    return data
    

# DISPLAY_Protection
def extract_display_protection(data: pd.DataFrame, inplace: bool=False):
    if inplace == False:
        data = data.copy()
    
    # drop DISPLAY_Protection
    data.drop('DISPLAY_Protection', axis=1, inplace=True)

    return data

def extract_display(data: pd.DataFrame, inplace: bool=False):
    if inplace == False:
        data = data.copy()
    
    extract_display_type(data, inplace=True)
    extract_display_size(data, inplace=True)
    extract_display_resolution(data, inplace=True)
    extract_display_protection(data, inplace=True)

    return data

