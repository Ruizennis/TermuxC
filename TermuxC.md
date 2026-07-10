# TermuxC
## Also known as TermuxCopy

this package was made to solve an issue with termux, not allowing copying to device clipboard easily without their companion app. This package solves that.

## Usage:

### Copy text
```python
from TermuxC import Copy
Copy(text)
```

### Copy from file
```python
from TermuxC import Copy
with open(Filename, "r", encoding="utf-8") as f:
    content = f.read()
    Copy(content)
```
## Requirements:
**Python 3+**

Get Python from https://www.python.org!

## Aware:
If using terminal multiplexers such as **Tmux** or **Screen** ensure they allow **OSC 52**.