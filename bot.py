# -*- coding: utf-8 -*-
import requests

TOKEN = '8085378567:AAFEoD2gxVn3SB5T1oAUacfyZhE-1YsNUyM'
CHAT_ID = '80889799'
message = 'Test message from Python bot!'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
data = {'chat_id': CHAT_ID, 'text': message}
response = requests.post(url, data=data)

print(response.json())