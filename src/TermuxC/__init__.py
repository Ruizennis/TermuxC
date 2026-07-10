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
help = {'-h', '--help', '-help'}
help_message = '''
Usage:

Copying text with cli
termuxc Test!
OR
echo "test" | Termuxc

Copying a number with cli
termuxc 1

Copying filecontents with cli
cat Filename | Termuxc
(replace filename with desired file path)

Using pip package to copy text
from TermuxC import Copy
Copy('test')

Using pip package to copy number
from TermuxC import Copy
Copy(1)

Using Pip package to text copy from file
from TermuxC import Copy
with open(filename, 'r') as F:
    C = F.read()
    Copy(C)
 
for more help see https://github.com/Ruizennis/TermuxC
'''
lock = Lock()

def Copy(string):
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        sys.stdout.write(f"\033]52;c;{b64}\a")
        sys.stdout.flush()
        sleep(Sleeptime)

def main():
  if not sys.stdin.isatty():
        readstdin = sys.stdin.read()
        if readstdin.endswith('\n'):
          readstdin = readstdin[:-1]
        if readstdin:
           Copy(readstdin)
           sys.exit(0)
        else:
          print('Please provide an input')
          sys.exit(0)
  elif help.intersection(sys.argv):
    print(help_message)
    sys.exit(0)
  elif len(sys.argv) > 1:
        Copy(' '.join(sys.argv[1:]))
        sys.exit(0)
  else:
    print('Please provide atleast 1 argument or run termuxc --help for help.')
    sys.exit(0)
