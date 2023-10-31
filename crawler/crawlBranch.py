import yaml


with open('crawler\config.yaml', 'r') as f:
    config = yaml.safe_load(f)

print(config['BranchUrl'])

