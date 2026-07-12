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
