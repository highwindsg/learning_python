#!/usr/bin/env python3

def moveDisk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height -1, fromPole, withPole, toPole)    # Recursive
        moveDisk(fromPole, toPole)
        moveTower(height -1, withPole, toPole, fromPole)    # Recursive

moveTower(30, 10, 0, 1)

