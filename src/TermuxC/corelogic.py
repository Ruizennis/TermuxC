import os
import sys
import base64
import logging

logger = logging.getLogger("TermuxC")

# tmux support natively


def check_for_tmux():
    """Check for TMUX in environment variables, returns True if found."""
    return "TMUX" in os.environ


def tmux_support(b64):
    """Return a tmux-compatible ANSI code if user is using tmux

    Runs the check_for_tmux function to check if user is using tmux
    if user is found to be using tmux, checks for
    the command that allows clipboard passthrough
    if command is not found, asks the user to add it manually.
    """
    multiplexor = check_for_tmux()
    if multiplexor:
        tmux_path = os.path.expanduser('~/.tmux.conf')
        file_content = ''
        if os.path.exists(tmux_path):
            with open(tmux_path, 'r', encoding='utf-8') as file_read:
                file_content = file_read.read()
        if "allow-passthrough" not in file_content:
            logger.warning(
                "Please add 'set -g allow-passthrough on' to your tmux "
                "configuration file to allow tmux support, as without "
                "explicitly allowing clipboard passthrough on OSC 52 "
                "is blocked and copying will fail."
            )

            logger.warning('Attempting to copy anyway..')
        # special tmux osc command
        return f"\033Ptmux;\033\033]52;c;{b64}\a\033\\"
    else:
        return f"\033]52;c;{b64}\a"


def copy(string: str | int | float) -> None:
    """Copies the text to the device clipboard with ANSI escape codes.

    Converts input into string then encodes it and gets thr write code
    and writes it to stdout
    then flushes the stdout to ready the stdout for more copy() calls.
    """
    content = str(string)
    b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
    write_code = tmux_support(b64)
    sys.stdout.write(write_code)
    sys.stdout.flush()
