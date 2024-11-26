import curses
from curses import wrapper
from time import sleep
import msvcrt
key = ''
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    key = stdscr.getch()
wrapper(main)
print(key)

# stdscr.clear()
# stdscr.refresh()