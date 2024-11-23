#Import Modules
import tk
import requests
import json

#Define headers for HTTP READ Request
headers = {
        "x-auth-token": 'df948511ec87f935f06f1c9ecb18f622'
        }

#Use requests module to get device info from libre
data = requests.get('http://10.0.1.6/api/v0/devices', headers=headers, verify=False)

#Convert data to json format
data = data.json()

#Make json format readable
#readabledata = json.dumps(data, indent=4)
#print (readabledata)

#Note: .items() method used on 'data' variable creates an iterable that allows you to loop through each key-value pair. This is commonly used in loops or when you need both the keys and values from a dictionary.

#Loop through key,value pairs in data.items():
for key,value in data.items():
    #if the type of the value is a list, loop through the dictionary within the list
    if type(value) == type(list()):
        for val in value:
            print ('System Hostname: ' + val['sysName'])
            print ('Location: ' + val['location'])
