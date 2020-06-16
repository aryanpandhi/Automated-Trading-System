import alpaca_trade_api as tradeapi

APCA_API_KEY_ID = 'PKW28DNPAGUH4TDZIL73'
APCA_API_SECRET_KEY = 'ecv8EUMV8zQmIilkUChHyOBRD/02eyYNVVfN03C6'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(APCA_API_KEY_ID,APCA_API_SECRET_KEY,APCA_API_BASE_URL)
account = api.get_account()
print(account)