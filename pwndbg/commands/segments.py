import gdb

import pwndbg.commands
import pwndbg.gdblib.regs


class segment(gdb.Function):
    """Get the flat address of memory based off of the named segment register."""

    def __init__(self, name) -> None:
        super(segment, self).__init__(name)
        self.name = name

    def invoke(self, arg=0):
        result = getattr(pwndbg.gdblib.regs, self.name)
        return result + arg


segment("fsbase")
segment("gsbase")


@pwndbg.commands.ArgparsedCommand("Prints out the FS base address. See also $fsbase.")
@pwndbg.commands.OnlyWhenRunning
def fsbase() -> None:
    """
    Prints out the FS base address. See also $fsbase.
    """
    print(hex(int(pwndbg.gdblib.regs.fsbase)))


@pwndbg.commands.ArgparsedCommand("Prints out the GS base address. See also $gsbase.")
@pwndbg.commands.OnlyWhenRunning
def gsbase() -> None:
    """
    Prints out the GS base address. See also $gsbase.
    """
    print(hex(int(pwndbg.gdblib.regs.gsbase)))
