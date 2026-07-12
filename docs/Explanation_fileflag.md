# The file flag
##### **Last Updated Jul 12 2026**
## This flag is used to copy text from a file instead of the default behaviour of text only

### Code used to check for file flag and copy text from file
```python
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
```