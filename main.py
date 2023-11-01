from crawler import crawlBrandsData, crawlDevicesUrl, crawlAllPhoneSpecs
import yaml


def main():
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # get Brands name, url and Number of devices
    crawlBrandsData(config)

    # get all devices url
    crawlDevicesUrl(config)

    # get all devices specs
    crawlAllPhoneSpecs(config)

    print('-' * 30)
    print('Done!')


if __name__ == '__main__':
    main()
