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
from msvcrt import kbhit,getch

entry_array = [['']]

cursor_x,cursor_y = 0,0

running = True

# key_bindings = {
#     b'\x08':'whatever bksp does',
#     b'enter':'goto newline (add new array to entry_array and set cursor to it)',
#     b'space':'end current word and go to the next',
#     b'ctrl+s':'save doc',
#     b'ctrl+z':'revert entry back to clean slate',
# }

while running:
    key = getch()

    try:
        if key == b'\x1b':
            running = False
        elif key == b'\x0d':
            entry_array.append([''])
            cursor_y += 1
            cursor_x = 0
        else:
            alpha_numeric = key.decode('ascii')
            if alpha_numeric == ' ':
                cursor_x += 1
                entry_array[cursor_y].append('')
            else:
                entry_array[cursor_y][cursor_x] = entry_array[cursor_y][cursor_x] + alpha_numeric
    except UnicodeDecodeError:
        running = False

print('\n'.join([' '.join(i) for i in entry_array]))