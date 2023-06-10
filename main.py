import argparse

from notes_exec import add_note, edit_note, list_notes, remove_note
from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise argparse.ArgumentTypeError('Некорректный формат даты - должно быть YYYY-MM-DD')

def main():
    parser = argparse.ArgumentParser(usage='python main.py [-h] [-a] [-l] [-d DATE] [-e EDIT] [-r REMOVE]', description='Note register app')
    parser.add_argument("-a", "--add", help="Add a new note", action="store_true")
    parser.add_argument("-l", "--list", help="List all notes", action="store_true")
    parser.add_argument("-d", "--date", help='Filter notes by date (format: YYYY-MM-DD)', type=parse_date)
    parser.add_argument("-e", "--edit", help="Edit a note", type=int)
    parser.add_argument("-r", "--remove", help="Remove a note", type=int)
    
    args = parser.parse_args()

    if args.add:
        add_note()
    elif args.list:
        list_notes(args.date)
    elif args.edit:
        edit_note(args.edit)
    elif args.remove:
        remove_note(args.remove)
    else:
        parser.print_help()
        print("No command entered. Use --help for help menu.")
        
if __name__ == '__main__':
    main()