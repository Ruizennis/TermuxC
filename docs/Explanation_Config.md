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