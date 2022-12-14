#!/usr/bin/env python
"""A simple cmd2 application."""
import cmd2


class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
    def __init__(self):
        super().__init__()

        # Make maxrepeats settable at runtime
        self.maxrepeats = 3
        self.add_settable(cmd2.Settable('maxrepeats', int, 'max repetitions for speak command', self))



if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())