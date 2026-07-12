# check_for_tmux()
##### **Last Updated Jul 12 2026**
## Below is the code that checks for the word TMUX in your environment and if its found returns True which is read in the Tmuxsupport function to determain what code to return to Copy()
```python
# tmux support natively
def check_for_tmux():
   if "TMUX" in os.environ:
     return True #using tmux
   else:
      return False #normal code
```

# Tmuxsupport section
```python
def Tmuxsupport(b64):
    multiplexor = check_for_tmux()
    if multiplexor:
        tmuxpath = os.path.expanduser('~/.tmux.conf')
        Fcontent = ''
        if os.path.exists(tmuxpath):
            with open(tmuxpath, 'r') as file_read:
                Fcontent = file_read.read()
        if not "allow-passthrough" in Fcontent:
            Yes_list = ['Y', 'YE', 'YES']
            if input("Allow script to add 'set -g allow-passthrough on' to your tmux.conf file to allow tmux support? [Y/n]").upper() in Yes_list:
                with open(tmuxpath, 'a') as file:
                    file.write("\nset -g allow-passthrough on\n")
                    try:
                        subprocess.run("tmux", "source-file", tmuxpath,
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL,
                                   check=True
                                  )
                    except subprocess.CalledProcessError as error:
                        print(f'Error, command failed with an error. Error: {error}')
            else:
                print("Please add 'set -g allow-passthrough on' to your tmux configuration file to allow tmux support, as without explicitly allowing clipboard passthough on OSC 52 is blocked and copying will fail.")
                print('Attempting to copy anyways..')
        return f"\033Ptmux;\033\033]52;c;{b64}\a\033\\" # special tmux osc command
    else:
        return f"\033]52;c;{b64}\a"
```
# Code Explanation
## Basically the code below checks for tmux with the multiplexor equals line and if it detects your using termux it then moves on to checking if you have a tmux.conf file at ~/.tmux.conf which it checks if you have clipboard passthrough enabled and if not it asks if you will allow it to add it for you and if you allow it then it adds it and if not prompts you to manualy add it then tries to run even without it.
