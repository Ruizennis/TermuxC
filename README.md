# TermuxC 
### Termux copy to clipboard made easy.
## Also known as TermuxCopy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/TermuxC.svg?color=blue)](https://pypi.org/project/TermuxC/)
[![PyPI downloads](https://img.shields.io/pypi/dm/TermuxC.svg)](https://pypi.org/project/TermuxC/)


This dual function pip package/cli tool was made to solve an issue with Termux, not allowing copying to device clipboard easily without their companion app. This package solves that.

## Cli Tool Usage:

### Copy text
```bash
termux text
```
**Or**
```bash
echo "test" | termuxc
```
### Copy text from file
```bash
cat filename | termuxc
```
### Copy current working directory
```bash
pwd | termuxc
```
Also compatable with
- bat
- grep
- curl
- head
- tail
## Pip package Usage:

### Copy text
```python
from TermuxC import Copy
Copy("Str") #works with strings,
Copy(1) # numbers
Copy(1.3) # and floats!
```

### Copy text from file
```python
from TermuxC import Copy
with open("TermuxC.py", "r") as f:
    content = f.read()
    Copy(content)
```
### Copy current working directory
```python
from TermuxC import Copy
import os
Copy(os.getcwd())
```

## Installation 
Install pip package
```bash
pkg install TermuxC
```

## Uninstallation
```bash
pip uninstall TermuxC
```

## Requirements:
**Python 3+**

Get Python from https://www.python.org!

View Package here https://pypi.org/project/TermuxC/2.0.5/

## Aware:
If using terminal multiplexers such as **Tmux** or **Screen** ensure they allow **OSC 52**.

### Tmux support
run this command to allow tmux to write to device clipboard
```bash
CONFIG_FILE=$( [ -d "$HOME/.config/tmux" ] \
  && echo "$HOME/.config/tmux/tmux.conf" \
  || echo "$HOME/.tmux.conf" ) ; \
printf "\n# Enable clipboard and passthrough\nset -s set-clipboard on\nset -g allow-passthrough on\n" >> "$CONFIG_FILE" \
&& tmux kill-server 2>/dev/null \
|| true
```

### Screen support
run this command to allow Screen to write to clipboard
```bash
CONFIG_FILE=$( [ -f "$HOME/.screenrc" ] \
  && echo "$HOME/.screenrc" \
  || echo "$HOME/.screenrc" ) ; \
printf "\n# Enable clipboard and passthrough\nregister [ \"\nbind ] paste [\n" >> "$CONFIG_FILE" \
&& screen -wipe >/dev/null 2>&1 \
|| true
```