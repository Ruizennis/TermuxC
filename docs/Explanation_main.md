# Main()
##### **Last Updated Jul 12 2026**
## This function handles flags and the cli
### For the code explanation the different parts or "chunks" are going to be explained then the function as a whole and its purpose

### Main code:
```python
def main():
    if not sys.stdin.isatty():
        readstdin = sys.stdin.read()
        if readstdin.endswith('\n'):
            readstdin = readstdin[:-1]
        if readstdin:
           Copy(readstdin)
           sys.exit(0)
        else:
          print('Please provide an input', file=sys.stderr)
          sys.exit(1)
    elif Vflags.intersection(sys.argv):
        try:
            Version = version('TermuxC')
            print(Version)
            sys.exit(0)
        except PackageNotFoundError:
                print('Error, pip package not found.')
                sys.exit(1)
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
  
    elif len(sys.argv) > 1:
        if iflags.intersection(args):
            try:
                print('[Interactive Mode - Enter text and press Ctrl+D to copy]')
                text = sys.stdin.read()
                if text.endswith('\n'):
                    text = text[:-1]
                Copy(text)
               sys.exit(0)
            except KeyboardInterrupt:
                print('Ctrl+C pressed, stopping')
                sys.exit(0)
            except:
                sys.exit(1)
        elif fileflags.intersection(args):
            try:
                fileR = args.index('-f') if '-f' in args else args.index('--file')
                args.pop(fileR)
                if not args:
                    print('Error, no file specified.')
                    sys.exit(1)
                file = args[0]
            except Exception as e:
                print(f'Error proccesing flags, {e}')
                sys.exit(1)
            if not os.path.isfile(file):
                print(f'Error, invalid filepath \"{file}\"', file=sys.stderr)
                sys.exit(1)
            try:
                with open(file, 'r') as filecopy:
                    Copy(filecopy.read())
            except PermissionError:
                print('Error, Unable to open file because of missing permision.')
            except:
                print(f'Error, failed to copy file {file}', file=sys.stderr)
        else:
            Copy(' '.join(sys.argv[1:]))
            sys.exit(0)
    else:
        print('Please provide at least 1 argument or run termuxc --help for help.', file=sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    main()
```
# Chunk 1: Checking for Interactive environment
## The first check in the code, `if not sys.stdin.isatty()` checks for an interactive environment like a terminal if its a Interactive environment, skip this block, an example would be piping data in (non interactivr) vs running the command directly (interactive) 
```python
    if not sys.stdin.isatty():
        readstdin = sys.stdin.read()
        if readstdin.endswith('\n'):
            readstdin = readstdin[:-1]
        if readstdin:
           Copy(readstdin)
           sys.exit(0)
        else:
          print('Please provide an input', file=sys.stderr)
          sys.exit(1)
```
# Chunk 2: Check for -V flag
## This next chunk checks for any version flags and if any are found then it attempts to prinr the current installed version of TermuxC, this can fail if the package was not installed on pypi however.
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
### See [version flag](Explanation_versionflag.md) For more information on how the version flag works.

# Chunk 3: Check for the help flag
# This Chunk checks for the help flag (See [help flag](Explanation_helpflag.md)) and if found prints help_messenge from the configuration variables and then asks if the user.would like to go to the github repository, Decided in configuration variables (See [Config](Explanation_Config.md))
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

# Chunk 4: Check for interactive flag
## This chunk checks for the interactive flag and runs the code if it is found in args, (See [InteractiveFlag](Explanation_interactiveflag.md))
```python
    elif len(sys.argv) > 1:
        if iflags.intersection(args):
            try:
                print('[Interactive Mode - Enter text and press Ctrl+D to copy]')
                text = sys.stdin.read()
                if text.endswith('\n'):
                    text = text[:-1]
                Copy(text)
               sys.exit(0)
            except KeyboardInterrupt:
                print('Ctrl+C pressed, stopping')
                sys.exit(0)
            except:
                sys.exit(1)
```
# Chunk 5: Check for file flag
## This chunk checks for the file flag and runs the code if it is found in args, (See [FileFlag](Explanation_fileflag.md))
```python

```