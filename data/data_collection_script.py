from datetime import date

import pandas as pd
import nsepy

"""
    Script to get past 10 year Nifty 50 index historical data.
    Modify start and end date to get data for different time duration.
"""
today = date.today()
nifty_data = nsepy.get_history(symbol="NIFTY",
                               start=date(year=today.year - 10, month=today.month, day=today.day - 3),
                               end=date.today(),
                               index=True)
nifty_data.to_csv('./StockPricePrediction/data/nifty_data.csv')
