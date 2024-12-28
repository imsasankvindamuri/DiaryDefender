# from curses import wrapper
# import curses

# def main(stdscr):
#     # Clear screen
#     disp_list = [f"10 divided by {i} is {10/i}\n" for i in range(1,11)]
#     stdscr.clear()
#     stdscr.scrollok(True)

#     for i in range(10):
#         stdscr.addstr(disp_list[i])
#         stdscr.refresh()
#         curses.napms(1000)
    
#     stdscr.getkey()

# wrapper(main)

import curses
from curses import wrapper

buffer = [[]]
final_text = ''

def bksp() -> None:
    #delete last element
    pass

def newline() -> None:
    #goto new line
    pass

def context_window(array) -> None:
    #makes sure that the diary doesn't exceed given terminal size
    pass


def main(stdscr):
    global buffer
    global final_text

    spcl_chars = {
        curses.KEY_BACKSPACE : bksp,
        curses.KEY_ENTER : newline,
    }

    stdscr.clear()
    
    while True:
        c = stdscr.getch()
        
        if c in spcl_chars:
            spcl_chars[c](context_window(buffer))

        else:
            #add element to the buffer
            pass

        stdscr.clear()
        stdscr.addstr(context_window(buffer))

wrapper(main)