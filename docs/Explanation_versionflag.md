# Version Flags
##### **Last Updated Jul 12 2026**
# They are checked for against the list provided in the configuration variable Vflags by default, the code checks for the flags in the cli in the main function
#### Flag checking code for checking the Vflags list:
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
# Custom Flag aliases
## By modifiyng the __init__.py file of the package you can add custom aliases for any flag easily, for example to add "version" as a flag you just have to add it to the pre configured list
```python
Vflags = {'-V', '--version', 'version'}
```
## Now termuxc version would be a valid command to show version, Note: this is not the case by default, see [readme.md](https://github.com/Ruizennis/TermuxC/blob/main/README.md) for default flags.
# Purpose
## By default the cli is setup to automaticaly print the package version and exit with an error code of 0 if the -V flag is used and the package was found by version(), if package is not found then exits with status code 1.