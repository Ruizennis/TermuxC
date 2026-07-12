# Contributing to TermuxC

Thank you for your interest in TermuxC! As this is a stable, lightweight utility, I appreciate contributions that maintain its minimalist design and security standards.

## Reporting Issues
If you encounter bugs or have feature requests, please check the [Issue Tracker](https://github.com/Ruizennis/TermuxC/issues) to ensure the issue hasn't already been reported. When opening a new issue, please include:
* **Environment**: Your Android version, Termux version, and terminal multiplexer (if applicable).
* **Steps to Reproduce**: A clear, concise description of how to trigger the issue.

## Pull Requests
I welcome pull requests that improve functionality and/or documentation. To ensure your changes are accepted:
1. **Maintain Scope**: Keep the package lightweight. Avoid adding heavy dependencies.
2. **Security First**: Ensure all new code adheres to the security practices outlined in the [Documentation](https://Ruizennis.github.io/TermuxC/) (e.g., using `subprocess` instead of os.system()).
4. **Documentation**: If you add a new flag or feature, please update the relevant tables in the README and technical documentation.

## Average bug testing
These are the standard tests recommended when adding a feature or modifying TermuxC:
- **Flag Handling**: Do flags correctly handle missing arguments (e.g., `termuxc -f` with no filename)?
- **Pipe Handling**: Does `cat file | termuxc` work as expected, including edge cases like empty files or files ending without a newline?
- **Concurrency**: Does running multiple `termuxc` commands in rapid succession trigger any race conditions? (Ensure the `lock` is properly utilized).
- **Tmux Integration**: If `tmux` is active, does the tool correctly detect the configuration or prompt for the necessary `allow-passthrough` setting?
- **Error Codes**: Does the tool consistently exit with code `1` for failures (e.g., missing file, invalid path) and code `0` for success?
- **Base64 Integrity**: Does the Base64 encoding handle special characters, spaces, and binary-like strings without breaking the OSC 52 sequence?

## Development Setup
If you wish to test changes locally:
1. Install custom installation of TermuxC
3. Test changes and complete average bug testing if applicable
4. Upload Instalation to github