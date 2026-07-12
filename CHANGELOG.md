# TermuxC Pip Changelog
## Note, this does not include all commits, only commits with an assosiated pip version increase.

---

# 2.5.6:
## Stable release
- fixed flags system by declaring args = set(sys.argv) on line 99
- Updated docs with new catpucchin mocha color scheme
- Removed 2.5.5 from stable releases list in docs.
---

# 2.5.5
- Fixed minor indentation error on line 141
- Updated documentation
- Updated README.md
- Added CONTRIBUTING.md

---

# 2.5.3
- Updated README.md to feature new version flag and fixed grammar mistakes

---

# 2.5.2
- -f flag reader updated
- New Version flag added
- Better except error handling
- Made code more readable


---

# 2.5.0
- File flag is more robust causing less errors and making it easier to use and more reliable
- Multiple minor bugs fixed
- Code is more readable
- Updated Pypi package by linking CHANGELOG.md
- Updated README.md by linking CHANGELOG.md and updating flags section

---

# 2.4.5
- Fixed minor bugs
- Replaced force text flag with interactive flag

---

# 2.4.3
## Fixed an inverse if statement at line 103

---

# 2.4.2:
## Fixed indentation error on line 81

---

# 2.4.1: 
- Added user confirmation step before writing to tmux config
- Removed all dependency on termux-setup-tools by instead using subproccess to activate the android activity manager
- Imported subproccess
- Linked changelog in pyproject.toml

---

# 2.2.6:
- Minor bug fixes
- Changed "help" to "helpflags"
- Added "-h", "-f", "-t" flags (help, force file, force text)

---

# 2.2.4:
- Added type annotations to Copy()

---

# 2.2.3:
- Updated readme.md
- Fixed bugs in tmuxsupport()

---

# 2.2.0:
- Added native tmux support
- Removed Screen focused integration instead opting to focus on tmux intergrarion only
- Updated README.md

---

# 2.0.9:
- Minor bug fixes across files like README.md, __init__.py and added build/ to .gitignore
- Removed Dist/ from .gitignore

---

# 2.0.6:
- Updated README.md
- Added dist/ to .gitignore

---

# 2.0.5:
- Added extra data to pyproject.toml
- Updated README.md
- Added Dist/ to .gitignore

---

# 2.0.0:
# Initial Pypi release