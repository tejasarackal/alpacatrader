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

clock = tradeapi.get_clock()
print(f"The market id {'open' if clock.is_open else 'close'}")
