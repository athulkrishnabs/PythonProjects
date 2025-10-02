
import json

entries = {"user_text":"",
           "user_length":""}

entry_text = input("Enter Here: ")

entry_length = len(entry_text)

entries["user_text"] = entry_text
entries["user_length"] = entry_length

try:
    with open("entries.json","r") as f:
        data = json.load(f)

except FileNotFoundError:
    data = {"entries":[]}       

data["entries"].append(entries)

with open("entries.json","w") as f:
    json.dump(data,f,indent=4)   

    print("Entry has been saved")


for i,e in enumerate(data["entries"],1):
    print(f"{i}.{e['user_text']} = {e['user_length']} characters")    

  






