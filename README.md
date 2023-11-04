# gmsarena-crawler

A simple crawler to get all the phones spec from gsmarena.com

## How to use

### 1. Install the requirements

```bash
pip install -r requirements.txt
```

### 2. Install the edge webdriver

```bash
sudo apt install msedgedriver
```

Or download it from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### 3. Run the crawler

```bash
python main.py
```

## How it works

### Step 1: Get all the brands

The first step is to get all the brands from the [brands page](https://www.gsmarena.com/makers.php3)

### Step 2: Find all the phones from each brand

The second step is using selenium to get url of all the phones from each brand page

### Step 3: Get the specs of each phone

The third step is to get the specs of each phone from the url we got in the second step

# Note

At step 3, you should use a proxy to avoid being banned by gsmarena.com or divide into multiple batches (recommended each batch has less than 2000 phones) to run the crawler
