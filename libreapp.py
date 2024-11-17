import requests
import json

headers = {
        "x-auth-token": 'df948511ec87f935f06f1c9ecb18f622'
        }

data = requests.get('http://10.0.1.6/api/v0/devices', headers=headers, verify=False)

data = data.json()

readabledata = json.dumps(data, indent=4)

print(readabledata)
