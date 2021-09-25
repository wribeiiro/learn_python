import requests

headers = {
    'User-agent': 'Ubuntu',
    'Referer': 'https://google.com'
}

cookies = {
    'last-visit': '10-10-2020'
}

data = {
    'username': 'ubuntu',
    'password': 'ubuntu'
}

request = None

try:
    request = requests.post('https://putsreq.com/04nYMdYGdaqQ0yTKoIKn', 
        headers=headers,
        cookies=cookies,
        data=data
    )
except Exception as e:
    print('Chama o amir', e)

print(request)