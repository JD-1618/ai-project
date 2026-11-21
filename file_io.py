import json
from functions import greet_learner
#1. handle a missing-file error gracefully
try:
    with open("missing _data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print ("file not found! Creating fresh 'profile...")
    data= {"name": "JD" , "city":"pune", "XP": 150}
    #2. write and read a JSON file 
    with open ("summary.json", "w") as f:
        json.dump(data, f, indent=4)
    with open ("summary.json", "r") as f:
     saved = json.load(f)
#3. Use the function imported from your own module (functions.py)
print(greet_learner(saved["name"], saved["city"]))
