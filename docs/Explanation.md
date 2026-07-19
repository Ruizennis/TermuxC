# TermuxC Docs
### **Last updated 6/18/2026**
---

# Security & Transparency
## Why is base64 used?
The OSC 52 protocol requires Base64-encoded input to prevent control characters (such as ";") from interfering with terminal escape sequences. Using base64.b64encode ensures input data is safely serialized, preventing malformed inputs or command injection vectors.  

Does the code contain obfuscation?  
No. All logic is transparent, and dependencies are limited to the Python Standard Library. 
The use of base64 is strictly for data transmission (OSC 52 compliance), not for masking malicious behavior.  
## System Security
- Input Handling: All user-provided text is sanitized and Base64 encoded before being written to stdout, ensuring data safety. 

Sources
- [Clipboards and terminals](https://dev.to/djmitche/clipboards-terminals-and-linux-3pk5)
- [xterm codes](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html)

---

# All functions should have proper error handling
## One example is the Version flag

### Version Flag code
```python
    elif args.version:
        try:
            package_version = version("TermuxC")
            print(package_version)
            sys.exit(0)
        except PackageNotFoundError:
            logger.error(
                "Pip package not found. To resolve this error, "
                "please install the package from PyPI with: "
                "pip install TermuxC"
            )
            sys.exit(1)
```
## PackageNotFoundError handles the exception if it cannot find the package, this can happen if the file isn't installed through pip.

---

## When forking this repository ensure the GitHub url points to **your** repository.

```python
GITHUB_URL = "https://github.com/Ruizennis/TermuxC"

```

|Configuration Variable| Controls|
|----------------------|---------|
| GITHUB_URL           | Controls what url is shown when using repository flag|

---

# Stable patches
|Version & Url | Installation Command | 
|-----------------|----------------------|
|[3.1.0](https://pypi.org/project/TermuxC/3.1.0/)| pip install termuxc==3.1.0|
|[3.0.0](https://pypi.org/project/TermuxC/3.0.0/)| pip install TermuxC==3.0.0|

### Click a version number navigate to that versions PyPi release.

### If you have any issues using the TermuxC package or cli tool please make an issue.