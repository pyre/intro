#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved

# rewrite as a pyre app
import pyre


# requirements for plot compatible function
class functor(pyre.protocol, family="plot.functors"):
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
        return quadratic

# an implementation of the functor protocol
class quadratic(pyre.component, family="plot.functors.quadratic"):
    """
    The function x -> a x^2 + b x + c
    """

    # user configurable state
    a = pyre.properties.int(default=1)
    b = pyre.properties.int(default=0)
    c = pyre.properties.int(default=0)

    # requirements
    @pyre.export
    def eval(self, x):
        """
        Invoke me on {x} and return the result
        """
        # unpack
        a = self.a
        b = self.b
        c = self.c
        # do what my name says...
        return a * x**2 + b * x + c


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
