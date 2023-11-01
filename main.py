from crawler import crawlBrandsData, crawlDevicesUrl
import yaml


def main():
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlBrandsData(config)

    crawlDevicesUrl(config)


if __name__ == '__main__':
    main()
