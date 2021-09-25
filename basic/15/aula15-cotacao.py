import requests
import json 
import datetime
import time

while True:
    try:
        response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacao = json.loads(response.text)

        print('### COTAÇÃO ### ', datetime.datetime.now())
        print('Dólar:', cotacao['USDBRL']['bid'])
        print('Euro:', cotacao['EURBRL']['bid'])
        print('BTC:', cotacao['BTCBRL']['bid'])

        time.sleep(2)
    except Exception as e:
        print('Chama o amir', e)
