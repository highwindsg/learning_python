#!/usr/bin/env python3

"""
Recursion is a method of solving problems by breaking the problem
up into smaller and smaller pieces until it can be easily solved.
Recursive algorithms rely on functions that call themselves.
Any problem you can solve iteratively, can be solved recursively;
however sometimes a recursive algorithm is a more elegant solution.

You write a recursive algorithm inside of a function. The function
must have a base case: a condition that ends a recursive algorithm
to stop it from continuing forever.

Inside the function, the function calls itself.
Each time the function calls itself, it moves closer to the base
case. Eventually, the base case condition is satisfied, the
problem is solved, and the function stops calling itself.

As algorithm that follows these rules satisfies the three laws
of recursion:
    1. A recursive algorithm must have a base case.
    2. A recursive algorithm must change its state and move
    toward the base case.
    3. A recursive algorithm must call itself, recursively.
Note: https://interactivepython.org/runestone/static/pythonds/Recursion/TheThreeLawsofRecursion.html
"""

def bottles_of_beer(bob):
    """Prints 99 Bottle of Beer on the Wall lyrics.
    :param bob: Must be a positive integer.
    'bob' is read as 'bottles of beer'."""

    # The 'if' statemt below is the first law of recursion
    # that sets the following base case to check when 'bob'
    # becomes less than 1.
    if bob < 1:
        print("""No more
                bottles
                of beer
                on the wall.
                No more
                bottles of
                beer.""")
        return  # When the var 'bob' becomes less than 1, the
                # function returns and stops calling itself.

    tmp = bob

    # The line 'bob -= 1' satisfies the second law of recursion
    # by decrementing the var 'bob' thus moving toward your
    # base case.
    bob -= 1
    print("""{} bottles of
            beer on the
            wall. {} bottles
            of beer. Take one
            down, pass it
            around, {} bottles
            of beer on the
            wall.""".format(tmp, tmp, bob)
          )

    # The line below satisfies the final law of recursion.
    """This line ensures that as long as the base case is not
    satisfied, the function will call itself. Each time the
    function calls itself, it passes itself a param that has
    been decremented by 1, and thus moves toward the base case.
    The first time the function calls itself (line 48),
    it will pass itself 98 as a param, then 97, then 96, until
    finally, it passes itself a param less than 1, which
    satisfies the base case being set.
    """
    bottles_of_beer(bob)


# Client calls function bottles_of_beer() with param 99.
bottles_of_beer(99)
