# TermuxC aka Termux copy, view TermuxC.md for more info
import base64
import sys

def Copy(string):
    content = str(string)
    b64 = base64.b64encode(content.encode()).decode()
    sys.stdout.write(f"\033]52;c;{b64}\a")
    sys.stdout.flush()