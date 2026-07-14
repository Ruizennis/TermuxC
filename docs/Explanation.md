# Advanced Explanation
### **Last updated 6/14/2026**
---

# Security & Transparency
## Why is base64 used?
The OSC 52 protocol requires Base64-encoded input to prevent control characters (such as ";") from interfering with terminal escape sequences. Using base64.b64encode ensures input data is safely serialized, preventing malformed inputs or command injection vectors.  

Does the code contain obfuscation?  
No. All logic is transparent, and dependencies are limited to the Python Standard Library. 
The use of base64 is strictly for data transmission (OSC 52 compliance), not for masking malicious behavior.  
## System Security
- Command Execution: The tool avoids os.system in favor of the subprocess module, mitigating the risk of shell injection.  
- Input Handling: All user-provided text is sanitized and Base64 encoded before being written to stdout, ensuring data safety. 

Sources
- [Clipboards and terminals](https://dev.to/djmitche/clipboards-terminals-and-linux-3pk5)
- [xterm codes](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html)

# All functions should have proper error handling
## One example is the Version flag

### Version Flag code
```python
    elif args.version:
        try:
            package_version = version('TermuxC')
            print(package_version)
            sys.exit(0)
        except PackageNotFoundError:
            print('Error, pip package not found, to resolve this error please install the package from Pypi with pip install TermuxC')
            sys.exit(1)
```
## PackageNotFoundError handles the exception if it cannot find the package, this can happen if the file isn't installed through pip.
## Install the package through Pypi with pip install TermuxC
---

## When forking this repository ensure the GitHub url points to **your** repository.

```python
GITHUB_URL = "https://github.com/Ruizennis/TermuxC"

```

|Configuration Variable| Controls|
|---------------------|--------|
| GITHUB_URL          | Controls what url is shown in help and what url to open when ActivityManager attempts to open repository url|

---


# General Troubleshooting Guide and Package limitations
## The Sections below should provide a quick way to fix any problems you may have, most problems should be solvable in a few small steps because of the nature of the program.

## **However** if you are using an old or unsupported multiplexor or a terminal that does not support osc 52 then these solutions may not work.

# Tmux Specific Fixes
|------|-------------|
|Copying not working|Ensure your tmux configuration file has "set -g allow-passthrough on"|


# Stable patches
|Installation Url | Installation Command | Version number |
|-----------------|----------------------|----------------|
|[TermuxC - 2.6.2](https://pypi.org/project/TermuxC/2.6.2/)| pip install TermuxC==2.6.2| 2.6.2|


##### If you have any issues using the TermuxC package or cli tool please make an issue.