from datetime import datetime
from prompt_toolkit import prompt
import sys
import os

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
    filename = input("Please enter the date of the entry you would like to delete in DD-MM-YYYY format: ") + ".txt"
    try:
        if os.path.exists(filename):
            confirm = input(f"Are you sure you want to delete the entry for {filename[:-4]} [y/n]? ").lower()

            if confirm == 'y':
                os.remove(filename)
                print(f"Deletion of entry on date {filename[:-4]} successful!")
            else:
                print("Returning to Diary...")
        else:
            print(f'''{filename[:-4]} has no entry.
Please check if you are entering in DD-MM-YYYY format,
And also check if you are using hyphens (-) rather than slashes (/).''')
    except Exception as e:
        print(f"Oops! An Exception Occurred...\n{e}")

def edit_entry():
    """This edits an existing entry"""
    filename = input("Please enter the date of the entry you would like to edit in DD-MM-YYYY format: ") + ".txt"
    try:
        if os.path.exists(filename):
            confirm = input(f'''Please note that this entails overriding all of your previous entries in this file.
Are you sure you want to redo the entry for {filename[:-4]} [y/n]? ''').lower()

            if confirm == 'y':
                with open(filename,"w") as file:
                    now = datetime.now()
                    file.write(f"{now.strftime("%A, %d-%m-%Y\n%H%M Hours\n")}")
                with open(filename,"a+") as file:
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

            else:
                print("Returning to Diary...")
        else:
            print(f'''{filename[:-4]} has no entry.
Please check if you are entering in DD-MM-YYYY format,
And also check if you are using hyphens (-) rather than slashes (/).''')
    except Exception as e:
        print(f"Oops! An Exception Occurred...\n{e}")


def view_entry():
    """This displays the index of all entries, and displays specific user-chosen entry in read-only mode"""
    entries = [f for f in os.listdir() if f.endswith('.txt')]
    if entries:
        print("Here are the existing entries: ")
        for i in entries:
            print(i)
        filename = input("Please enter the date of the entry you would like to edit in DD-MM-YYYY format: ") + ".txt"

        if filename in entries:
            print("Here is the entry in read-only mode. Press the enter key to exit...\n")
            with open(filename,"r") as file:
                print(file.read())
                placeholder = input()
        else:
            print("No such entry exists. Returning to Diary...")

    else:
        print("There are no entries. Returning to Diary...")

def exit_app():
    """Exits the app"""
    confirm = input("Are you sure [y/n]? ").lower()

    if confirm == 'y':
        print("Thanks for using the app!")
        sys.exit()
    else:
        print("Returning to Diary...")