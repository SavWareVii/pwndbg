import argparse

import pwndbg.color.message as message
import pwndbg.commands
import pwndbg.ghidra

parser = argparse.ArgumentParser(description="Decompile a given function using Ghidra.")
parser.add_argument(
    "func",
    type=str,
    default=None,
    nargs="?",
    help="Function to be decompiled. Defaults to the current function.",
)


@pwndbg.commands.OnlyWithFile
@pwndbg.commands.ArgparsedCommand(parser)
def ghidra(func) -> None:
    try:
        print(pwndbg.ghidra.decompile(func))
    except Exception as e:
        print(message.error(e))
