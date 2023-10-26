import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test!")
    stdscr.addstr("\nPress any key to start!")
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = "Hello Worls this is some test text for this app!"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        current_text.append(key)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
 
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
