# TermuxC 
### Termux copy to clipboard made easy.
## Also known as TermuxCopy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/TermuxC.svg?color=blue)](https://pypi.org/project/TermuxC/)
[![PyPI downloads](https://img.shields.io/pypi/dm/TermuxC.svg)](https://pypi.org/project/TermuxC/)


This dual function pip package & cli tool was made to solve an issue with Termux, not allowing copying to device clipboard easily without their companion app; This package solves that.

## Why use TermuxC?
- Allows coping from files or text
- Allows piping data
- Requires **Zero** dependencies
- Designed specifically to work on Termux


## Installation 
Install as pip package
```bash
pip install TermuxC
```
Install using git
```bash
git clone https://github.com/Ruizennis/TermuxC
cd TermuxC
```

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
### Copy text from file using the read from file flag
```bash
termuxc -f filename
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
from TermuxC import copy
copy("Str") # works with strings,
copy(1) # numbers
copy(1.3) # and floats!
```

### Copy text from file
```python
from TermuxC import copy
with open("filename", "r") as f:
    content = f.read()
    copy(content)
```
### Copy current working directory
```python
from TermuxC import copy
import os
copy(os.getcwd())
```

## Flags
|Flag|Function        |
|----|----------------|
| -f | Read from file |
| -i | Interactive mode|
| -h | Show help menu |
| -V | Show package version|
#### Additional flag aliases
- --file
- --interactive
- --help
- --version

## Handling special characters
### Some text may get interpreted incorrectly by the bash (or zsh) interpreter, to fix this issue wrap your text in single or double quotes

### Incorrect:
```
termuxc (
```
This will throw an error!
### Correct:
```
termuxc "("
```
This will copy the text successfully!

## Requirements:
**Python 3.10+**

View Package here!  
[Pypi - TermuxC](https://pypi.org/project/TermuxC/)

Create an issue here!  
[Issues](https://github.com/Ruizennis/TermuxC/issues)

View changelog here!  
[Changelog](https://github.com/Ruizennis/TermuxC/blob/main/CHANGELOG.md)

View the documentation here!  
[Documentation](https://Ruizennis.github.io/TermuxC/)

### Tmux support
#### To allow TermuxC to work inside of termux add "set -g allow-passthrough on" to your tmux configuration file.

# License
## This project is licensed under the MIT license, see [LICENSE](LICENSE)
