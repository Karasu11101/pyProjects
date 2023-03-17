import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.erase()
    stdscr.addstr("This is a typing-speed test program.")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)
    try:
        stdscr.addstr(10, 0, f"WPM: {wpm}")
    except curses.error:
        pass

    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        try:
            stdscr.addstr(0, i, char, color)
        except curses.error:
            pass


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.erase()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        str_text = "".join(current_text)
        if str_text == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    stdscr.addstr(2, 0, f"You completed the test! Your score is {wpm} WPM. ")


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "Do you want to repeat the test? Press any key to restart the test, or ESC to quit. ")
        key = stdscr.getkey()
        if ord(key) == "27":
            break

wrapper(main)
