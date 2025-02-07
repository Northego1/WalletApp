import requests

URL = 'http://127.0.0.1:8000/api/v1/wallets/2274ebb1-f4be-41f7-b317-be42f26dd26/operation'
DATA = {
    'operationType': 'DEPOSIT',
    'amount': 1000
}


def send():
    request = requests.post(url=URL, json=DATA)
    return request.json()


print(send())
