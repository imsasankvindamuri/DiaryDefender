# import sqlite3 as sql
# import sys

# connection = sql.connect("diary.db")

# cursor = connection.cursor()

# cursor.execute('''

# create table if not exists entries(
#     id integer primary key autoincrement,
#     date text not null,
#     title text,
#     content text not null
#     )

# ''')

# connection.commit()
# connection.close()

# print("Type some stuff. Once done, press Ctrl+D (Ctrl+Z if windows) and press Enter to confirm: ")
# s = sys.stdin.read()
# print(s)
import os
import sys
from msvcrt import getch

entry_array = ['']

undo_array = []

cursor_x,cursor_y = 0,0

running = True

def display(array) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("".join(array))

def savedoc(array) -> None:
    confirm = input("Are you sure [y/n]? ").lower()
    if confirm == 'y':
        with open("hello.txt","a+") as file:
            file.write("".join(array))
        sys.exit()
    else:
        print("Returning to Diary...")

key_bindings = {
    b'\x08':lambda array,undo_array = undo_array: undo_array.append(array.pop()) if array else None,
    b'\x0d':lambda array: array.append("\n"),
    b'\x1b':savedoc,
    b'\x1a':lambda array, undo_array = undo_array: array.append(undo_array.pop()) if undo_array else None,
}

while running:
    display(entry_array)
    key = getch()

    try:
        if key in key_bindings:
            key_bindings[key](entry_array)
        else:
            alpha_numeric = key.decode('ascii')
            entry_array.append(alpha_numeric)
    except UnicodeDecodeError:
        running = False

display(entry_array)