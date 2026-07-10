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
##Installation (Just Package)
Install Package and add to site-packages
```bash
curl -fsSL https://raw.githubusercontent.com/Ruizennis/TermuxC/main/TermuxC.py -o $(python -m site --user-site)/TermuxC.py
```
Uninstall Package
```bash
rm $(python -m site --user-site)/TermuxC.py
```

## Installation (Entire Repository)
Install git
```bash
pkg install git -y
```
Clone the repository and move it
```bash
git clone https://github.com/Ruizennis/TermuxC
cd TermuxC
```
Install Package as pip package
```bash
pip install -e .
```
Uninstall Package
```bash
pip uninstall TermuxC
```
## Requirements:
**Python 3+**

Get Python from https://www.python.org!

## Aware:
If using terminal multiplexers such as **Tmux** or **Screen** ensure they allow **OSC 52**.