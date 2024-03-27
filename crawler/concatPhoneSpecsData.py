import os
import yaml
import pandas as pd


def concatPhoneSpecsData(config):
    path = config["SavePath"]

    # list all data files in path
    files = os.listdir(path)
    files = [file for file in files if file.startswith(
        config["DevicesSpecsFileName"]) and "temp" not in file]
    files = sorted(files, key=lambda x: (len(x), x))

    # concat all data files
    df = pd.concat([pd.read_csv(os.path.join(path, file))
                    for file in files], ignore_index=True)

    # save to csv
    df.to_csv(os.path.join(
        path, config["DevicesSpecsFileName"] + ".csv"), index=False)


if __name__ == '__main__':
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    concatPhoneSpecsData(config)
