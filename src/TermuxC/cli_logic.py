import os
import sys
import logging
import argparse
from .corelogic import copy
from importlib.metadata import version, PackageNotFoundError
GITHUB_URL = "https://github.com/Ruizennis/TermuxC"

logger = logging.getLogger("TermuxC")
lock = Lock()


def handle_stdin():
    """Handles piped input."""
    read_stdin = sys.stdin.read().rstrip('\n')
    if not read_stdin:
        logger.warning('Please provide an input')
        sys.exit(1)
    return read_stdin


def flag_interactive():
    """handles interactive flag logic"""
    try:
        print('[Interactive Mode - Enter text and press Ctrl+D to copy]')
        text = sys.stdin.read().rstrip('\n')
        if not text.strip():
            logger.warning("Error, no input provided.")
            sys.exit(1)
        return text
    except KeyboardInterrupt:
        print('Ctrl+C pressed, stopping')
        sys.exit(0)


def flag_file(filepath: str) -> str:
    """Handles copying text from file"""
    if not os.path.isfile(filepath):
        logger.warning(f'Error, invalid filepath \"{filepath}\"')
        sys.exit(1)
    try:
        with open(filepath, 'r', encoding='utf-8') as file_copy:
            return file_copy.read()
    except PermissionError:
        logger.warning(
            'Error, Unable to open file because of'
            'missing permission.'
        )
        sys.exit(1)


def main():
    """Handles command-line arguments."""
    logging.basicConfig(
        level=logging.WARNING,
        format="%(levelname)s: %(message)s"
        )
    parser = argparse.ArgumentParser(
        description="Termux copy to clipboard made easy using OSC 52.")
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help=(
            "Shows installed TermuxC package version and exits"
        )
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help=(
            "Enables interactive mode, "
            "Note: interactive mode forces text only input."
        )
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Copies text from a file")
    parser.add_argument(
        "-r",
        "--repository",
        action="store_true",
        help="Shows the projects github repository")
    parser.add_argument("text", nargs="*")
    args = parser.parse_args()
    if not sys.stdin.isatty():
        content = handle_stdin()
    elif args.version:
        try:
            package_version = version('TermuxC')
            print(package_version)
            sys.exit(0)
        except PackageNotFoundError:
            logger.warning(
                "Error: Pip package not found. To resolve this error, "
                "please install the package from PyPI with: "
                "pip install TermuxC"
            )
            sys.exit(1)
    elif args.repository:
        print(f"Visit {GITHUB_URL} for the project repository.")
        sys.exit(0)
    elif args.interactive:
        content = flag_interactive()
    elif args.file:
        content = flag_file(args.file)
    elif args.text:
        content = ' '.join(args.text)
    else:
        logger.warning(
            "Please provide at least 1 argument or run "
            "termuxc --help for help.")
        sys.exit(1)
    copy(content)
