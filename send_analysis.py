# -*- coding: utf-8 -*-
import requests

TOKEN = '8085378567:AAFEoD2gxVn3SB5T1oAUacfyZhE-1YsNUyM'
CHAT_ID = '80889799'

# Sample analysis (dummy data)
symbol = "BTC/USDT"
entry = "66200"
target = "68000"
stop = "64900"
leverage = 10
risk = "5%"
position = "Long"

message = f"""
Trade Signal
-------------
Symbol: {symbol}
Position: {position}
Entry Price: {entry}
Take Profit: {target}
Stop Loss: {stop}
Leverage: {leverage}x
Risk: {risk}
"""

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
data = {'chat_id': CHAT_ID, 'text': message}

response = requests.post(url, data=data)
print(response.json())