import os
from datetime import datetime
import pytz
from prompt_toolkit import prompt

def add_entry():
    """This checks for if a given entry exists. If it does, it opens that entry. Else, It makes a new one."""
    now = datetime.now()

    with open(f"{now.strftime("%d-%m-%Y")}.txt","a+") as file:
        file.write(f"{now.strftime("%A, %d-%m-%Y\n%H%M Hours\n")}")
        print("Please enter your entry. Once done, type `!s` on a newline to confirm your entry:\n")
        entry_lines = []
        while True:
            line = input()
            if line == '!s':
                print("Here is the saved entry:\n")
                print("\n".join(entry_lines))
                break
            else:
                entry_lines.append(line)
        entry = "\n".join(entry_lines) + "\n"
        file.write(entry)

def del_entry():
    """This deletes an entry if it exists"""
    pass

def edit_entry():
    """This edits an existing entry"""
    pass

def view_entry():
    """This displays the index of all entries, and displays specific user-chosen entry in read-only mode"""
    pass

def exit_app():
    """Exits the app"""
    confirm = input("Are you sure [y/n]? ").lower()

    if confirm == 'y':
        print("Thanks for using the app!")
        exit()
    else:
        print("Returning to Diary...")