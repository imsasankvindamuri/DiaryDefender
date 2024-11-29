from datetime import datetime
import pytz
from prompt_toolkit import prompt
from diary_funcs import *
import sys
import os


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
                '1': view_entry,
                '2': add_entry,
                '3': del_entry,
                '4': edit_entry,
                '5': exit_app,
            }
            
            action = actions.get(selector)
            if action:
                action()
            else:
                print("Invalid Input. Please Choose a proper option.")

        except KeyboardInterrupt:
            print("\nProcess Interrupted. Exiting Program...")
            sys.exit()