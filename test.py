import os
from msvcrt import getch

entry_array = ['']
cursor_row, cursor_col = 0, 0
running = True

def display(array) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n".join(array))

def bksp(array) -> None:
    global cursor_row
    if array[cursor_row] == '':
        if cursor_row > 0:
            array.pop()
            cursor_row -= 1
        else:
            None
    else:
        array[cursor_row] = array[cursor_row][:-1]

def nwline(array) -> None:
    global cursor_row
    array.append('')
    cursor_row += 1

def savedoc(array) -> None:
    global running
    confirm = input("Are you sure [y/n]? ").lower()
    if confirm == 'y':
        with open("hello.txt","a+") as file:
            file.write("\n".join(array))
        running = False
    else:
        print("Returning to Diary...")

key_bindings = {
    b'\x08':bksp,
    b'\x0d':nwline,
    b'\x13':savedoc,
}

while running:
    display(entry_array)
    key = getch()

    try:
        if key in key_bindings:
            key_bindings[key](entry_array)
        else:
            alpha_numeric = key.decode('ascii')
            entry_array[cursor_row] = entry_array[cursor_row] + alpha_numeric
    except UnicodeDecodeError:
        running = False

display(entry_array)