#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved

# rewrite as a pyre app
import pyre


# requirements for plot compatible function
class functor(pyre.protocol):
    """
    A new type of configurable state that captures functions that can be plotted
    """

    # requirements
    @pyre.provides
    def eval(self, x):
        """
        Invoke me on {x} and return the result
        """

    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        # square is the default
        return square

# an implementation of the functor protocol
class square(pyre.component):
    """
    The function x -> x^2
    """

    # requirements
    @pyre.export
    def eval(self, x):
        """
        Invoke me on {x} and return the result
        """
        # do what my name says...
        return x**2


# my app
class Plot(pyre.application):
    """
    Tabulate the values of a function
    """

    # user configurable state
    func = functor()
    limit = pyre.properties.int(default=5)

    # the main entry point
    def main(self):
        """
        Tabulate a function
        """
        # make a table
        for x in range(self.limit):
            # of the squares of some values
            print(f"{x:2}^2 = {self.func.eval(x):2}")
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
