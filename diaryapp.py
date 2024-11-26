import os
from datetime import datetime
import pytz
from prompt_toolkit import prompt

entries_dir = "C:\DiaryDefender\diaryentries"

def addEntry():
    """This checks for if a given entry exists. If it does, it opens that entry. Else, It makes a new one."""
    pass

def delEntry():
    """This deletes an entry if it exists"""
    pass

def editEntry():
    """This edits an existing entry"""
    pass

def dispEntries():
    """This displays the index of all entries, and displays specific user-chosen entry in read-only mode"""
    pass

def exitDiary():
    """Exits the app"""
    confirm = input("Are you sure [y/n]? ").lower()

    if confirm == 'y':
        print("Thanks for using the app!")
        exit()
    else:
        print("Returning to Diary...")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Hi! This is my first attempt at a diary app!")
    
    while True:
        try:
            selector = input('''
Please choose one of the below options:
1. Display the current entries
2. Add a new entry
3. Delete a specific entry
4. Edit a specific entry
5. Exit the diary
''')
            actions = {
                '1': dispEntries,
                '2': addEntry,
                '3': delEntry,
                '4': editEntry,
                '5': exitDiary,
            }
            
            action = actions.get(selector)
            if action:
                action()
            else:
                print("Invalid Input. Please Choose a proper option.")

        except KeyboardInterrupt:
            print("\nProcess Interrupted. Exiting Program...")
            exit()