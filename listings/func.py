#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# factor our the function we are tabulating

# my function
def square(x):
    """
    A function
    """
    # do what my name says...
    return x**2

# bootstrap
if __name__ == "__main__":
    # make a table
    for x in range(5):
        # of the squares of some values
        print(f"{x:2}^2 = {square(x):2}")

# end of file
