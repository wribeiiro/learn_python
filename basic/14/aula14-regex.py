import re
import requests 

req = requests.get('https://www.wribeiiro.com')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)

if padrao:
    print(padrao)
else:
    print('padrao nao encontrado')