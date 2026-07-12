# TermuxC aka Termux Copy, view README.md for more info
# Copyright (c) 2026 Ruizennis
# This software is licensed under the MIT License.
# See the LICENSE file or https://opensource.org/licenses/MIT for full terms.
import base64
import sys
import os
from threading import Lock
import subprocess
from importlib.metadata import version, PackageNotFoundError
# configuration
Githuburl = "https://github.com/Ruizennis/TermuxC"
helpflags = {'-h', '--help'}
fileflags = {'-f', '--file'}
iflags = {'-i', '--interactive'}
Vflags = {'-V', '--version'}
help_message = f'''
Usage:

Copying text with cli
termuxc <text>
OR
echo "<text>" | Termuxc

Copying a number with cli
termuxc <number>

Copying filecontents with cli
cat <file> | Termuxc

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
-f • Force File read
-i • Interactive Mode
-h • Show help menu
-V • Show version info

for more help see {Githuburl}
'''
# tmux support natively
def check_for_tmux():
   if "TMUX" in os.environ:
     return True #using tmux
   else:
      return False #normal code

def Tmuxsupport(b64):
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
                    try:
                        subprocess.run("tmux", "source-file", tmuxpath,
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL,
                                   check=True
                                  )
                    except subprocess.CalledProcessError as error:
                        print(f'Error, command failed with an error. Error: {error}')
            else:
                print("Please add 'set -g allow-passthrough on' to your tmux configuration file to allow tmux support, as without explicitly allowing clipboard passthrough on OSC 52 is blocked and copying will fail.")
                print('Attempting to copy anyways..')
        return f"\033Ptmux;\033\033]52;c;{b64}\a\033\\" # special tmux osc command
    else:
        return f"\033]52;c;{b64}\a"

lock = Lock()

def Copy(string: str | int) -> None:
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        write_code = Tmuxsupport(b64)
        sys.stdout.write(write_code)
        sys.stdout.flush()

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
    elif Vflags.intersection(sys.argv):
        try:
            Version = version('TermuxC')
            print(Version)
            sys.exit(0)
        except PackageNotFoundError:
                print('Error, pip package not found.')
                sys.exit(1)
    elif helpflags.intersection(sys.argv):
        print(help_message)
        print('Would you like to open the Github Repository in browser? [Y/n]')
        pick = input().upper()
        if pick in ['Y', 'YE', 'YES']:
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
        if iflags.intersection(args):
            try:
                print('[Interactive Mode - Enter text and press Ctrl+D to copy]')
                text = sys.stdin.read()
                if text.endswith('\n'):
                    text = text[:-1]
                Copy(text)
                sys.exit(0)
            except KeyboardInterrupt:
                print('Ctrl+C pressed, stopping')
                sys.exit(0)
            except:
                sys.exit(1)
        elif fileflags.intersection(args):
            try:
                fileR = args.index('-f') if '-f' in args else args.index('--file')
                args.pop(fileR)
                if not args:
                    print('Error, no file specified.')
                    sys.exit(1)
                file = args[0]
            except Exception as e:
                print(f'Error processing flags, {e}')
                sys.exit(1)
            if not os.path.isfile(file):
                print(f'Error, invalid filepath \"{file}\"', file=sys.stderr)
                sys.exit(1)
            try:
                with open(file, 'r') as filecopy:
                    Copy(filecopy.read())
            except PermissionError:
                print('Error, Unable to open file because of missing permission.')
            except Exception as error:
                print(f'Error, failed to copy file {file}, error: {error}', file=sys.stderr)
        else:
            Copy(' '.join(sys.argv[1:]))
            sys.exit(0)
    else:
        print('Please provide at least 1 argument or run termuxc --help for help.', file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    main()