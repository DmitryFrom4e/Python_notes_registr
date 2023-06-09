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
    
def list_notes(date):
    with open(NOTES_FILE, "r") as f:
        data = json.load(f)
        
    if date:
        notes = [note for note in data["notes"] if note["date"] == date]
    else:
        notes = data["notes"]
        
    if len(notes) == 0:
        print("No notes found!")
    else:
        for note in notes:
            print("="*30)
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Message: {note['message']}")
            print(f"Date: {note['date']}")