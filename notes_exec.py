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
        str_date = date.isoformat()
        notes = [note for note in data["notes"] if str(note["date"]).startswith(str_date)]
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
            
def edit_note(note_id):
    with open(NOTES_FILE, "r") as f:
        data = json.load(f)
        
    note_found = False
    
    for note in data["notes"]:
        if note["id"] == note_id:
            title = input("Enter new title: ")
            message = input("Enter new message: ")
            note["title"] = title
            note["message"] = message
            note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_found = True
            break
    
    if not note_found:
        print(f"Note with the ID {note_id} was not found")
    else:
        with open(NOTES_FILE, "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Note {note_id} edited successfully!")
        
def remove_note(note_id):
    with open(NOTES_FILE, "r") as f:
        data = json.load(f)
        
    note_found = False
    
    for note in data["notes"]:
        if note["id"] == note_id:
            data["notes"].remove(note)
            note_found = True
            
    if not note_found:
        print(f"Note with the ID {note_id} was not found")
    else:
        with open(NOTES_FILE, "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Note with the ID {note_id} removed successfully!")