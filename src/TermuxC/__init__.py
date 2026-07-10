# TermuxC aka Termux copy, view README.md for more info
# Copyright (c) 2026 Ruizennis
# This software is licensed under the MIT License.
# See the root LICENSE file or https://opensource.org/licenses/MIT for full terms.
import base64
import sys
from time import sleep
from threading import Lock
# configuration
Sleeptime = 0.5

lock = Lock()

def Copy(string):
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        sys.stdout.write(f"\033]52;c;{b64}\a")
        sys.stdout.flush()
        sleep(Sleeptime)
