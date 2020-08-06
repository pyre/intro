#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved

# rewrite as a pyre app
import pyre


# my function; still not a member, but there is a plan...
def square(x):
    """
    A function
    """
    # do what my name says...
    return x**2


# my app
class Plot(pyre.application):
    """
    Tabulate the values of a function
    """

    # the {limit} is now a pyre property, with a type and a default value
    limit = pyre.properties.int(default=5)

    # the main entry point
    def main(self):
        """
        Tabulate a function
        """
        # make a table
        for x in range(self.limit):
            # of the squares of some values
            print(f"{x:2}^2 = {square(x):2}")
        # indicate success, à la u*ix
        return 0


# bootstrap
if __name__ == "__main__":
    # tell pyre this app wants to play by giving it a name
    app = Plot(name="plot")
    # invoke
    status = app.run()
    # share the exit code with the shell
    raise SystemExit(status)


# end of file
