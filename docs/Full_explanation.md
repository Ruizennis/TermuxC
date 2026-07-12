# Full Explanation
## This is the Full Explanation of every main part of the code
---
# Imports
## In this section I will explain what packages are imported and what they are used for in the code.
##### **Last Updated Jul 12 2026**

# Heres the code for Imports
```python
import base64
import sys
import os
from threading import Lock
import subprocess
from importlib.metadata import version, PackageNotFoundError
```
## Now we can start going down the list

# Base64
```python
def Copy(string: str | int) -> None:
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        write_code = Tmuxsupport(b64)
        sys.stdout.write(write_code)
        sys.stdout.flush()
```
## Base64 is used in the "Copy" function as seen above to covert the desired message to base64 using utf-8 encoding, this is because the Operating System Command the package uses (OSC 52) **requires** the entered message to be base64 encoded to ensure theres no acidental ';' which signal an EOF to the terminal and break the command, encoding in base64 before sending the messenge also prevents malformed inputs.
Sources
- [Clipboards and terminals](https://dev.to/djmitche/clipboards-terminals-and-linux-3pk5)
- [xterm codes](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html)
# Sys
## Sys is the libary used for the majority of parts related to flags in the code via sys.argv but there are other uses throughout below is a table of uses
|Command|Usage in the script|
|-------|-----|
|sys.argv|Used to check for flags and take user input|
|sys.exit()|Used to pass exit codes and exit program exit code 1 means an error occured 0 means nothing went wrong|
|sys.stdin.read()|Used to take whatever text user entered and use it in the script as a variable|
|sys.stdout.write()|Used to run the OSC that copya the desired text to clipboard|
|sys.stdout.flush()|Used to ensure desire text is copyied to clipboard and prepares the function for the next call|

# Os
## The os module is mainly used in this package for checking if a file is avalible to copy via os.path.isfile and os.path.exists

# Threading
## Threading is only used for the Lock() this makes the Copy function run on one thread thus preventing errors when running  multiple Copy calls in quick succsesion by making calls made while "locked" wait for it to "unlock" before running.

# Subprocess
## This module is used to replace os.system for running commands, this ensures that os command injection cant be done thus protecting against unwanted commands being ran on your device. this module is also.used to call activitymanager which is used to open the Githuburl in the help menu. see [Help Flag](Explanation_helpflag.md)

# from importlib.metadata
## This is used strictly for the -V or "version" flag to display the installed version if the package

### Version Flag code
```python
    elif Vflags.intersection(sys.argv):
        try:
            Version = version('TermuxC')
            print(Version)
            sys.exit(0)
        except PackageNotFoundError:
                print('Error, pip package not found.')
                sys.exit(1)
```
## PackageNotFoundError handles the exception if it cannot find the package, this can happen if the file isnt installed though pip

---

# Configuration
##### **Last Updated Jul 12 2026**
## Below is the configuration area of my code and also a table of what they do
## If you make a fork I **Highly** reccomend changing atleast the Githuburl so that it points to **your** repository.
```python
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
```

|Configuration Varible| Purpose|
|---------------------|--------|
| Githuburl           | Controls what url is shown in help and what url to open when am start url is ran in the help flag|
| helpflags | Controls help flag aliases|
| fileflags | Controls file read mode flag aliases|
| iflags | Controls Interactive mode flag aliases|
| Vflags | Controls Version flag aliases|
| help_message| Controls what is printed when a help flag is detected|

## Note: There is not a configuration variable to disable asking if you want to open the Githuburl when running a help flag to keep the package low bloat

---

# check_for_tmux()
##### **Last Updated Jul 12 2026**
## Below is the code that checks for the word TMUX in your environment and if its found returns True which is read in the Tmuxsupport function to determain what code to return to Copy()
```python
# tmux support natively
def check_for_tmux():
   if "TMUX" in os.environ:
     return True #using tmux
   else:
      return False #normal code
```

# Tmuxsupport section
```python
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
                print("Please add 'set -g allow-passthrough on' to your tmux configuration file to allow tmux support, as without explicitly allowing clipboard passthough on OSC 52 is blocked and copying will fail.")
                print('Attempting to copy anyways..')
        return f"\033Ptmux;\033\033]52;c;{b64}\a\033\\" # special tmux osc command
    else:
        return f"\033]52;c;{b64}\a"
```
# Code Explanation
## Basically the code below checks for tmux with the multiplexor equals line and if it detects your using termux it then moves on to checking if you have a tmux.conf file at ~/.tmux.conf which it checks if you have clipboard passthrough enabled and if not it asks if you will allow it to add it for you and if you allow it then it adds it and if not prompts you to manualy add it then tries to run even without it.

---

# Copy()
##### **Last Updated Jul 12 2026**
## The Copy function logic is split into other functions for readability thus making the function compact
## Allowed Arguments `str` | `num`

### Code
```python
def Copy(string: str | int) -> None:
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        write_code = Tmuxsupport(b64)
        sys.stdout.write(write_code)
        sys.stdout.flush()
```
# Purpose
## The purpose of the Copy function is to convert whatever argument entered into a string then convert it into base64 code for tmuxsupport to use when creating the write_code, once tmuxsupport returns the correct code then the function will continue by writing the code to the stdout which is what copys the text to your clipboard and flushes the stdout making sure it is ready for another copy call.

### Operations order
1. initial Call sent to Copy function
2. input is converted to `str`
3. `string` is converted to `base64`
4. `Base64` messenge is sent to tmuxsupport to evaluate what `write code` to return
5. Copy function recives proper `write code`
6. Write code is sent to `stdout` and messenge is copyied to clipboard
7. `stdout` is flushed and prepared for additional function calls

# See also:
## [TmuxSupport](Explanation_Tmuxsupport.md)

---

# Main()
##### **Last Updated Jul 12 2026**
## This function handles flags and the cli
### For the code explanation the different parts or "chunks" are going to be explained then the function as a whole and its purpose

### Main code:
```python
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
                print(f'Error proccesing flags, {e}')
                sys.exit(1)
            if not os.path.isfile(file):
                print(f'Error, invalid filepath \"{file}\"', file=sys.stderr)
                sys.exit(1)
            try:
                with open(file, 'r') as filecopy:
                    Copy(filecopy.read())
            except PermissionError:
                print('Error, Unable to open file because of missing permision.')
            except:
                print(f'Error, failed to copy file {file}', file=sys.stderr)
        else:
            Copy(' '.join(sys.argv[1:]))
            sys.exit(0)
    else:
        print('Please provide at least 1 argument or run termuxc --help for help.', file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    main()
```
# Chunk 1: Checking for Interactive environment
## The first check in the code, `if not sys.stdin.isatty()` checks for an interactive environment like a terminal if its a Interactive environment, skip this block, an example would be piping data in (non interactivr) vs running the command directly (interactive) 
```python
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
```
# Chunk 2: Check for -V flag
## This next chunk checks for any version flags and if any are found then it attempts to prinr the current installed version of TermuxC, this can fail if the package was not installed on pypi however.
```python
    elif Vflags.intersection(sys.argv):
        try:
            Version = version('TermuxC')
            print(Version)
            sys.exit(0)
        except PackageNotFoundError:
                print('Error, pip package not found.')
                sys.exit(1)
```
### See [version flag](Explanation_versionflag.md) For more information on how the version flag works.

# Chunk 3: Check for the help flag
# This Chunk checks for the help flag (See [help flag](Explanation_helpflag.md)) and if found prints help_messenge from the configuration variables and then asks if the user.would like to go to the github repository, Decided in configuration variables (See [Config](Explanation_Config.md))
```python
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
```

# Chunk 4: Check for interactive flag
## This chunk checks for the interactive flag and runs the code if it is found in args, (See [InteractiveFlag](Explanation_interactiveflag.md))
```python
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
```
# Chunk 5: Check for file flag
## This chunk checks for the file flag and runs the code if it is found in args, (See [FileFlag](Explanation_fileflag.md))
```python
        elif fileflags.intersection(args):
            try:
                fileR = args.index('-f') if '-f' in args else args.index('--file')
                args.pop(fileR)
                if not args:
                    print('Error, no file specified.')
                    sys.exit(1)
                file = args[0]
            except Exception as e:
                print(f'Error proccesing flags, {e}')
                sys.exit(1)
            if not os.path.isfile(file):
                print(f'Error, invalid filepath \"{file}\"', file=sys.stderr)
                sys.exit(1)
            try:
                with open(file, 'r') as filecopy:
                    Copy(filecopy.read())
            except PermissionError:
                print('Error, Unable to open file because of missing permision.')
            except:
                print(f'Error, failed to copy file {file}', file=sys.stderr)
        else:
            Copy(' '.join(sys.argv[1:]))
            sys.exit(0)
```

---

# Version Flags
##### **Last Updated Jul 12 2026**
# They are checked for against the list provided in the configuration variable Vflags by default, the code checks for the flags in the cli in the main function
#### Flag checking code for checking the Vflags list:
```python
    elif Vflags.intersection(sys.argv):
        try:
            Version = version('TermuxC')
            print(Version)
            sys.exit(0)
        except PackageNotFoundError:
                print('Error, pip package not found.')
                sys.exit(1)
```
# Custom Flag aliases
## By modifiyng the __init__.py file of the package you can add custom aliases for any flag easily, for example to add "version" as a flag you just have to add it to the pre configured list
```python
Vflags = {'-V', '--version', 'version'}
```
## Now termuxc version would be a valid command to show version, Note: this is not the case by default, see [readme.md](https://github.com/Ruizennis/TermuxC/blob/main/README.md) for default flags.
# Purpose
## By default the cli is setup to automaticaly print the package version and exit with an error code of 0 if the -V flag is used and the package was found by version(), if package is not found then exits with status code 1.

---

# Help Flags
##### **Last Updated Jul 12 2026**
## They are checked for against the list provided in the configuration variable helpflags by default, the code checks for the flags in the cli in the main function
#### Flag checking code for checking the helpflags list:
```python
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
```
# Custom Flag aliases
## By modifiyng the "\_\_init__.py" file of the package you can add custom aliases for any flag easily, for example to add "help" as a flag you just have to add it to the pre configured list
```python
helpflags = {'-h', '--help', 'help'}
```
## Now termuxc help would be a valid command to show help information, Note: this is not the case by default, see [readme.md](https://github.com/Ruizennis/TermuxC/blob/main/README.md) for default flags.

# Purpose
## By default the cli is setup to print the help messange then ask if you want to go to the set Githuburl (see [Config](Explanation_Config.md)) and if you answer yes it then uses activity manager to open the url in your default browser

# Default help messenge
## The default help messenge is as follows
```text
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
```
## The default help messenge can be changed by changing the configuration variable help_messenge.

---

# Interactive flag
##### **Last Updated Jul 12 2026**
## This flag makes it so the user can type any input directly into the sys.stdin

### Check for interactive flag (-i)
```python
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
```
## This flag when detected will print tbe messenge and allow the user to type into the sys.stdin, it then strips newlines for the osc and sends the text to the Copy function

# See also:
## [Copy Function](Explanation_Copy.md)

---

# The file flag
##### **Last Updated Jul 12 2026**
## This flag is used to copy text from a file instead of the default behaviour of text only

### Code used to check for file flag and copy text from file
```python
        elif fileflags.intersection(args):
            try:
                fileR = args.index('-f') if '-f' in args else args.index('--file')
                args.pop(fileR)
                if not args:
                    print('Error, no file specified.')
                    sys.exit(1)
                file = args[0]
            except Exception as e:
                print(f'Error proccesing flags, {e}')
                sys.exit(1)
            if not os.path.isfile(file):
                print(f'Error, invalid filepath \"{file}\"', file=sys.stderr)
                sys.exit(1)
            try:
                with open(file, 'r') as filecopy:
                    Copy(filecopy.read())
            except PermissionError:
                print('Error, Unable to open file because of missing permision.')
            except:
                print(f'Error, failed to copy file {file}', file=sys.stderr)
        else:
            Copy(' '.join(sys.argv[1:]))
            sys.exit(0)
```