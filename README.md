# TermuxC
## Also known as TermuxCopy

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
with open(TermuxC.py, "r") as f:
    content = f.read()
    Copy(content)
```
## Installation
Install git
```bash
pkg install git -y
```
Clone the repository
```bash
git clone https://github.com/Ruizennis/TermuxC
```
Add Export so that Pkg is avalible from anywhere
```bash
echo "export PYTHONPATH=\"\$PYTHONPATH:\$(pwd)\"" >> ~/.bashrc && source ~/.bashrc
```
## Requirements:
**Python 3+**

Get Python from https://www.python.org!

## Aware:
If using terminal multiplexers such as **Tmux** or **Screen** ensure they allow **OSC 52**.