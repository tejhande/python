import pandas as pd
import requests

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
response = requests.get(url)
data = response.json()

header = list(data["data"][0].keys())

records = []
for record in data["data"]:
    row = []
    for key in header:
        row.append(record[key])
    records.append(row)

df = pd.DataFrame(records, columns=header)

df.to_excel("nifty_50_stocks.xlsx", index=False)
