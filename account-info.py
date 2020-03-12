import alpaca_trade_api as tradeapi
import os

APCA_API_BASE_URL = os.environ['APCA_API_BASE_URL']
APCA_API_KEY_ID = os.environ['APCA_API_KEY_ID']
APCA_API_SECRET_KEY = os.environ['APCA_API_SECRET_KEY']

api = tradeapi.REST(
    base_url=APCA_API_BASE_URL,
    key_id=APCA_API_KEY_ID,
    secret_key=APCA_API_SECRET_KEY
)

account = api.get_account()

if account.trading_blocked:
    print('Account is currently blocked from trading.')

# check how much money we have left to open new positions
print(f'{account.buying_power} is available as buying power')


# summarize account
print(account)