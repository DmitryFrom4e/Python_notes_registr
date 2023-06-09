import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        data = {"notes": []}
        json.dump(data, f)

def add_note():
    title = input("Enter title: ")
    message = input("Enter message: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(NOTES_FILE, "r") as f:
        data = json.load(f)
        
    id = len(data["notes"]) + 1
    data["notes"].append({"id": id, "title": title, "message": message, "date": date})
    
    with open(NOTES_FILE, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Note with the ID {id} added successfully!")