# TermuxC 
### Termux copy to clipboard made easy.
## Also known as TermuxCopy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/TermuxC.svg?color=blue)](https://pypi.org/project/TermuxC/)
[![PyPI downloads](https://img.shields.io/pypi/dm/TermuxC.svg)](https://pypi.org/project/TermuxC/)


This dual function pip package & cli tool was made to solve an issue with Termux, not allowing copying to device clipboard easily without their companion app; This package solves that.

## Cli Tool Usage:

### Copy text
```bash
termuxc text
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
Also compatible with
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
pip install TermuxC
```

## Uninstallation
Uninstall pip package
```bash
pip uninstall TermuxC
```
## Flags
|Flag|Function        |
|----|----------------|
| -f | Read from file |
| -i | Interactive mode|
| -h | Show help menu |
| -V | Show package version|
#### Aditional flag alliases
- --file
- --interactive
- --help
- --version

## Requirements:
**Python 3+**

Get Python from here!  
https://www.python.org

View Package here!  
https://pypi.org/project/TermuxC/

Create an issue here!  
https://github.com/Ruizennis/TermuxC/issues

View changelog here!  
https://github.com/Ruizennis/TermuxC/blob/main/CHANGELOG.md

View the documentation here!  
https://Ruizennis.github.io/TermuxC/

### Tmux support
As of version **2.2.0 And above** TermuxC has native tmux support!

# License
## This project is licensed under the MIT license, see [LICENSE](LICENSE)
