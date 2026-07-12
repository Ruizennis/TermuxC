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