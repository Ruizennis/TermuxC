# TermuxC aka Termux copy, view README.md for more info
# Copyright (c) 2026 Ruizennis
# This software is licensed under the MIT License.
# See the LICENSE file or https://opensource.org/licenses/MIT for full terms.
import base64
import sys
import os
from time import sleep
from threading import Lock
import subprocess
# configuration
Sleeptime = 0.5
Githuburl = "https://github.com/Ruizennis/TermuxC"
helpflags = {'-h', '--help', '-help'}
help_message = f'''
Usage:

Copying text with cli
termuxc Test!
OR
echo "<text>" | Termuxc

Copying a number with cli
termuxc <number>

Copying filecontents with cli
cat <file> | Termuxc
(replace <file> with desired file path)

Using pip package to copy text
from TermuxC import Copy
Copy('<text>')

Using pip package to copy number
from TermuxC import Copy
Copy(<number>)

Using Pip package to text copy from file
from TermuxC import Copy
with open(filename, 'r') as F:
    C = F.read()
    Copy(C)
    
Flags
-f • Force File file
-t • Force text copy
-h • Show help menu

for more help see {Githuburl}
'''
#New: added tmux support natively
def check_for_tmux():
   if "TMUX" in os.environ:
     return True #using tmux
   else:
      return False #normal code
             

lock = Lock()

def Copy(string: str | int) -> None:
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        multiplexor = check_for_tmux()
        if multiplexor:
                tmuxpath = os.path.expanduser('~/.tmux.conf')
                Fcontent = ''
                if os.path.exists(tmuxpath):
                    with open(tmuxpath, 'r') as file_read:
                        Fcontent = file_read.read()
                if not "allow-passthrough" in Fcontent:
                    Yes_list = ['Y', 'YE', 'YES']
                    if input("Allow script to add 'set -g allow-passthrough on' to your tmux.conf file to allow tmux support? [Y/n]").upper() in Yes_list:
                        with open(tmuxpath, 'a') as file:
                            file.write("\nset -g allow-passthrough on\n")
                            os.system(f"tmux source-file {tmuxpath} >/dev/null 2>&1") 
                    else:
                        print("Please add 'set -g allow-passthrough on' to your tmux configuration file to allow tmux support, as without explicitly allowing clipboard passthough on OSC 52 is blocked and copying will fail.")
                        print('Attempting to copy anyways..')
            write_code = f"\033Ptmux;\033\033]52;c;{b64}\a\033\\" # special tmux osc command
        else:
            write_code = f"\033]52;c;{b64}\a"
        sys.stdout.write(write_code)
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
          print('Please provide an input', file=sys.stderr)
          sys.exit(1)
  elif helpflags.intersection(sys.argv):
    print(help_message)
    print('Would you like to open the Github Repository in browser? [Y/n]')
    pick = input()
    if pick not in ['y', 'Y', 'yes', 'Yes' '', ' ']:
        try:
            subprocess.run(
    ["am", "start", "-a", "android.intent.action.VIEW", "-d", Githuburl],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
            )
        except:
            print('Error, opening url failed please copy url manually into browser address bar.')
            print(Githuburl)
    sys.exit(0)
  elif len(sys.argv) > 1:
      if sys.argv[1] in ['-t', '--text']:
        text = sys.stdin.read()
        if text.endswith('\n'):
            text = text[:-1]
        Copy(text)
        sys.exit(0)

      elif sys.argv[1] in ['-f', '--file']:
          if len(sys.argv) == 3:
            file = sys.argv[2]
            if os.path.isfile(file):
                try:
                     with open(file, 'r') as filecopy:
                         Copy(filecopy.read())
                except:
                    print('Error, failed to copy file.', file=sys.stderr)
            else:
                print('Error, invalid filepath', file=sys.stderr)
                sys.exit(1)
                
          else:
              print('Error, -f flag requires a file', file=sys.stderr)
              sys.exit(1)
      else:
        Copy(' '.join(sys.argv[1:]))
        sys.exit(0)
  else:
    print('Please provide at least 1 argument or run termuxc --help for help.', file=sys.stderr)
    sys.exit(1)
