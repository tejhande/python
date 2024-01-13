import requests
import pandas as pd
from bs4 import BeautifulSoup
symbol=input("Enter Symbol: ")
# Get the data from the NSE website
url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+symbol
data = requests.get(url)

# Parse the data using BeautifulSoup
soup = BeautifulSoup(data.content, "html.parser")

# Extract the required information
last_price = soup.find("span", id="lastPrice").get_text().strip()
previous_close = soup.find("span", id="prevClose").get_text().strip()
open_price = soup.find("span", id="openPrice").get_text().strip()

# Save the data in Excel
df = pd.DataFrame({
    "Last Price": [last_price],
    "Previous Close": [previous_close],
    "Open Price": [open_price]
})
df.to_excel("INFY_stock_data.xlsx", index=False)


