from crawler import crawlBrandsData, crawlDevicesUrl, crawlAllPhoneSpecs, concatPhoneSpecsData, crawlAllPhoneSpecsMini
import yaml


def main():
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # get Brands name, url and Number of devices
    print('Step 1: Crawl Brands Data')
    run = input('Do you want to crawl Brands Data? (y/n): ')
    if run == 'y' or run == 'Y' or run == 'yes' or run == 'Yes' or run == 'YES':
        crawlBrandsData(config)

    print('-' * 30)

    # get all devices url
    print('Step 2: Crawl Devices Url')
    run = input('Do you want to crawl Devices Url? (y/n): ')
    if run == 'y' or run == 'Y' or run == 'yes' or run == 'Yes' or run == 'YES':
        crawlDevicesUrl(config)

    print('-' * 30)

    # get all devices specs
    print('Step 3: Crawl All Phone Specs')
    run = input('Do you want to crawl All Phone Specs? (y/n): ')
    if run == 'y' or run == 'Y' or run == 'yes' or run == 'Yes' or run == 'YES':
        start = input('Start from: ')
        end = input('End at (-1 for all): ')
        crawlAllPhoneSpecsMini(config, start, end)
        # crawlAllPhoneSpecs(config, start, end)

    print('-' * 30)

    # concat all data files
    run = input('Do you want to concat all data files? (y/n): ')
    if run == 'y' or run == 'Y' or run == 'yes' or run == 'Yes' or run == 'YES':
        concatPhoneSpecsData(config)

    print('-' * 30)
    print('All done!')
    print("You can find the data in", config["SavePath"], "folder")
    print("Thank you for using our crawler! <3")


if __name__ == '__main__':
    main()
