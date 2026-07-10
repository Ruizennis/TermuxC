# TermuxC aka Termux copy, view TermuxC.md for more info
import base64
import sys
from time import sleep
from threading import Lock

lock = Lock()

def Copy(string):
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode()).decode()
        sys.stdout.write(f"\033]52;c;{b64}\a")
        sys.stdout.flush()
        sleep(0.5)