import sys
from turtle import width
import clipboard
import json

SAVED_DATA = "data.json"

def save_data(path,data):
    with open(path,"w") as f:
        json.dump(data,f)


def load_data(path):
    try:
        with open(path,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    cmand = sys.argv[1]
    data = load_data(SAVED_DATA)

    if cmand == "save":
        key = input("Enter the key : ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data Saved ๐ฅณ")
    elif cmand == "load":
        key = input("Enter the key : ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard. ๐๐")
        else:
            print("Key doesn't exist. ๐ถ")
    elif cmand == "list":
        print(data)
    else:
        print("unknown command ๐")

else:
    print("No command is given. ๐คจ")