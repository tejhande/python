import pandas as pd
from nsepy import get_history
from nsepy.derivatives import get_expiry_date

symbol="NIFTY50"
def get_options_chain(symbol):
    expiry = get_expiry_date(year=2023, month=2)
    data = get_history(symbol=symbol,
                       start=expiry-pd.Timedelta(days=30),
                       end=expiry,
                       option_type='CE',
                       strike_price="17800",
                       expiry_date=expiry)
    return data

# Example usage
options_chain_data = get_options_chain('INFY')
options_chain_data.to_excel('options_chain_data.xlsx', index=False)
