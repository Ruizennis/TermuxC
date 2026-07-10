# TermuxC 
### Termux copy to clipboard made easy.
## Also known as TermuxCopy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This package was made to solve an issue with Termux, not allowing copying to device clipboard easily without their companion app. This package solves that.

## Usage:

### Copy text
```python
from TermuxC import Copy
Copy("Str")
Copy(1)
Copy(1.3)
```

### Copy from file
```python
from TermuxC import Copy
with open("TermuxC.py", "r") as f:
    content = f.read()
    Copy(content)
```
## Installation (Package only)
Install git
```bash
pkg install git
```
Install Package
```bash
pip install git+https://github.com/Ruizennis/TermuxC.git
```
Uninstall Package
```bash
pip uninstall TermuxC
```

## Installation (Entire Repository)
Install git
```bash
pkg install git
```
Clone the repository and move into it
```bash
git clone https://github.com/Ruizennis/TermuxC
cd TermuxC
```
Install pip Package
```bash
pip install -e .
```
Uninstall package
```bash
pip uninstall TermuxC
```

## Requirements:
**Python 3+**

Get Python from https://www.python.org!

## Aware:
If using terminal multiplexers such as **Tmux** or **Screen** ensure they allow **OSC 52**.
