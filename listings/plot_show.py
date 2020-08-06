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

    # user configurable state
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

    # verify that by the time the constructor is invoked, configuration is complete
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # print my configuration
        print(f"{self.pyre_name}.limit = {self.limit}")
        # all done
        return


# bootstrap
if __name__ == "__main__":
    # instantiate
    app = Plot(name="plot")
    # invoke
    status = app.run()
    # share the exit code with the shell
    raise SystemExit(status)


# end of file
