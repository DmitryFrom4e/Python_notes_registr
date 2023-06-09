import argparse

from notes_exec import add_note

def main():
    parser = argparse.ArgumentParser(usage='python main.py [-h] [-a] [-l] [-d DATE] [-e EDIT] [-r REMOVE]', description='Note register app')
    parser.add_argument("-a", "--add", help="Add a new note", action="store_true")
    
    args = parser.parse_args()

    if args.add:
        add_note()
    else:
        print("No command entered. Use --help for help menu.")
        
if __name__ == '__main__':
    main()