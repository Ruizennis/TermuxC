# Interactive flag
##### **Last Updated Jul 12 2026**
## This flag makes it so the user can type any input directly into the sys.stdin

### Check for interactive flag (-i)
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
## This flag when detected will print tbe messenge and allow the user to type into the sys.stdin, it then strips newlines for the osc and sends the text to the Copy function

# See also:
## [Copy Function](Explanation_Copy.md)