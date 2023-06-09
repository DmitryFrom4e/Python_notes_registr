import argparse

from notes_exec import add_note, list_notes, edit_note

def main():
    parser = argparse.ArgumentParser(usage='python main.py [-h] [-a] [-l] [-d DATE] [-e EDIT] [-r REMOVE]', description='Note register app')
    parser.add_argument("-a", "--add", help="Add a new note", action="store_true")
    parser.add_argument("-l", "--list", help="List all notes", action="store_true")
    parser.add_argument("-d", "--date", help="Filter notes by date")
    parser.add_argument("-e", "--edit", help="Edit a note", type=int)
    
    args = parser.parse_args()

    if args.add:
        add_note()
    elif args.list:
        list_notes(args.date)
    elif args.edit:
        edit_note(args.edit)
    else:
        print("No command entered. Use --help for help menu.")
        
if __name__ == '__main__':
    main()