from secrets import *
import pandas as pd
import alpaca_trade_api as tradeapi
from alpaca_trade_api.stream import Stream

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL)
#account = api.get_account()


print(api.get_barset('AAPL', 'minute').df)


#print(account.status)	
#api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df