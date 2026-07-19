import os
import sys
import base64
from time import sleep
import logging
from threading import Lock

logger = logging.getLogger(__name__)

lock = Lock()


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
        logger.info("Tmux environment detected.")
        tmux_path = os.path.expanduser("~/.tmux.conf")
        file_content = ""
        if os.path.exists(tmux_path):
            with open(tmux_path, "r", encoding="utf-8") as file_read:
                file_content = file_read.read()
        if "allow-passthrough" not in file_content:
            logger.error(
                "Please add 'set -g allow-passthrough on' to your tmux "
                "configuration file to allow tmux support, as without "
                "explicitly allowing clipboard passthrough on OSC 52 "
                "is blocked and copying will fail."
            )
            logger.info("Exiting..")
            sys.exit(1)

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
    with lock:
        content = str(string)
        if len(content) <= 100:
            logger.info(f'Copied \"{content}\"')
        else:
            logger.info(
                f"Copied {len(content)} characters. "
                "(Text too long to display)"
            )
        b64 = base64.b64encode(content.encode("utf-8")).decode("ascii")
        write_code = tmux_support(b64)
        sys.stdout.write(write_code)
        sys.stdout.flush()
        sleep(0.5)
