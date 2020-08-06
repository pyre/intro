#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved

# make an "app" by moving the generation of the table to a class


# my function; it is not a member since it doesn't need {self}
def square(x):
    """
    A function
    """
    # do what my name says...
    return x**2


# my app
class Plot:
    """
    Tabulate the values of a function
    """

    # the main entry point
    def run(self):
        """
        Tabulate a function
        """
        # make a table
        for x in range(5):
            # of the squares of some values
            print(f"{x:2}^2 = {square(x):2}")
        # indicate success, à la u*ix
        return 0


# bootstrap
if __name__ == "__main__":
    # instantiate
    app = Plot()
    # invoke
    status = app.run()
    # share the exit code with the shell
    raise SystemExit(status)


# end of file
