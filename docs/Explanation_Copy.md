# Copy()
##### **Last Updated Jul 12 2026**
## The Copy function logic is split into other functions for readability thus making the function compact
## Allowed Arguments `str` | `num`

### Code
```python
def Copy(string: str | int) -> None:
    with lock:
        content = str(string)
        b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
        write_code = Tmuxsupport(b64)
        sys.stdout.write(write_code)
        sys.stdout.flush()
```
# Purpose
## The purpose of the Copy function is to convert whatever argument entered into a string then convert it into base64 code for tmuxsupport to use when creating the write_code, once tmuxsupport returns the correct code then the function will continue by writing the code to the stdout which is what copys the text to your clipboard and flushes the stdout making sure it is ready for another copy call.

### Operations order
1. initial Call sent to Copy function
2. input is converted to `str`
3. `string` is converted to `base64`
4. `Base64` messenge is sent to tmuxsupport to evaluate what `write code` to return
5. Copy function recives proper `write code`
6. Write code is sent to `stdout` and messenge is copyied to clipboard
7. `stdout` is flushed and prepared for additional function calls

# See also:
## [TmuxSupport](Explanation_Tmuxsupport.md)