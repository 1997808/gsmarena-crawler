import os
import pandas as pd


def concat_data():
    path = os.getcwd() + '/tidy_data/seperate_data'
    files = os.listdir(path)
    files = [file for file in files if file.endswith('.csv')]
    if 'data.csv' in files:
        files.remove('data.csv')
    print(files)
    df = pd.DataFrame()
    for file in files:
        # Concat theo cot
        df = pd.concat([df, pd.read_csv(path + '/' + file)], axis=1)
    print("Bo du lieu co:", df.shape[1], "cot")
    df.to_csv(path + '/data.csv', index=False)


if __name__ == '__main__':
    concat_data()
