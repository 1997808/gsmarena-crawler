from crawler import crawlBrandsData, crawlDevicesUrl, crawlAllPhoneSpecs
import yaml


def main():
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    print('Step 1: Crawl Brands Data')
    # get Brands name, url and Number of devices
    crawlBrandsData(config)

    print('-' * 30)
    print('Step 2: Crawl Devices Url')
    # get all devices url
    crawlDevicesUrl(config)

    print('-' * 30)
    print('Step 3: Crawl All Phone Specs')
    # get all devices specs
    crawlAllPhoneSpecs(config)

    print('-' * 30)
    print('Done!')


if __name__ == '__main__':
    main()
