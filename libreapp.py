#Import Modules
import tkinter as tk
from tkinter import ttk
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
readabledata = json.dumps(data, indent=4)
print (readabledata)

#Note: .items() method used on 'data' variable creates an iterable that allows you to loop through each key-value pair. This is commonly used in loops or when you need both the keys and values from a dictionary.

#Loop through key,value pairs in data.items():
datafortable = []

for key,value in data.items():
    #if the type of the value is a list, loop through the dictionary within the list
    if type(value) == type(list()):
        for val in value:
            print ('System Hostname: ' + val['sysName'])
            print ('Location: ' + val['location'])
            datafortable.append(val['sysName'])
            datafortable.append(val['hostname'])
            datafortable.append(val['version'])
            datafortable.append(val['hardware'])
            datafortable.append(val['serial'])


#Create root window
root = tk.Tk()
 
#Root window title and dimension
root.title("LibrePoller")
#Set geometry (widthxheight)
root.geometry('1200x400')

#button = tk.Button(root, text="Click Me", command = root.destroy)
#button.pack(padx=20, pady=20)

columns = ('host_name', 'ip_add', 'software_ver', 'hardware', 'srl')

tree = ttk.Treeview(root, columns=columns, show='headings')

tree.heading('host_name', text='Hostname')
tree.heading('ip_add', text = 'IP Address')
tree.heading('software_ver', text = 'Software Version')
tree.heading('hardware', text = 'Hardware Model')
tree.heading('srl', text = 'Serial Number')

for items in datafortable:
    tree.insert('', tk.END, values=items)

tree.grid(row=0, column=0)

root.mainloop()
