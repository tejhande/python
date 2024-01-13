import requests
import pandas as pd
import time

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

def get_data():
    response = requests.get(url)
    data = response.json()
    return data

def update_data():
    data = get_data()
    df = pd.DataFrame(data["records"]["data"])
    df.to_excel("OptionChain.xlsx")

# Get the data for the first time
update_data()

# Automatically update the data every minute
while True:
    time.sleep(60)
    update_data()
