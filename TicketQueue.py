#!/usr/bin/env python3

# A queue can simulate people waiting in line to buy tickets for a movie.

import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    """
    Create a function called simulate_line which simulates selling tickets
    to a line of people. The function accepts two params.
    till_show - an int representing the number of secs until the show starts
                and there is no time left to buy tickets.
    max_time -  an int representing the longest amt of time (in secs) it
                takes for a person to buy a ticket.
    """
    def simulate_line(self, till_show, max_time):
        pq = Queue()    # Set var 'pq' (read as person queue) to class Queue().
        tix_sold = []   # Set var 'tix_sold' to an empty list first. This list
                        # will keep track of people who purchased a ticket.

        """Next you fill the queue with one hundred strings, starting with
        'person0' and ending with 'person99'. Each string in the queue
        represents a person in line waiting to buy a ticket."""
        for i in range(100):    # In the for_loop, iterate from 0 to 99, not
                                # inclusive of 100.
            pq.enqueue("person" + str(i))   # From pq, use the enqueue method
                                            # to pass in the param person with
                                            # concatenate of a string number
                                            # from the for_loop.

        """The built-in time module has a function called time(). It returns
        a float that represents the number of secs it has been since
        Jan 1 1970 using as a reference. If I call the time function right
        now, it returns the number of secs since epoch (Jan 1 1970). And if
        one sec I call it again, the float the function returns will be
        incremented by 1."""

        # The var 't_end' finds the result of the time() plus the number of
        # secs passed in as the var 'till_show'. Hence the combination of
        # the two created a point in the future.
        t_end = time.time() + till_show
        now = time.time()   # Set var 'now' to the current seconds.
        # The 'while_loop' runs until either the time() returns a result
        # greater than 't_end', or the 'pq' (person queue) is empty.
        while now < t_end and not pq.is_empty():
            now = time.time()   # Set var 'now' to the current seconds.
            # You stop Python from doing anything for a random number of secs
            # between 0 and max_time using the randint() method.
            r = random.randint(0, max_time) # Set var 'r' with a random int
                                            # from 0 to max_time)
            time.sleep(r)   # From time, call the sleep() method on var 'r'.
            person = pq.dequeue()   # Delist the front person in queue line
                                    # and set it to 'var' person.
            print(person)   # Print out the person being de-queued from the
                            # queue line.
            tix_sold.append(person) # Get the 'tix_sold' list and call the
                                    # append() method, and pass in the
                                    # value of var 'person'.

        # Then return the value of person in the 'tix_sold' list to the
        # 'simulate_line' function.
        return tix_sold


queue = Queue() # Set var 'queue' to a class of Queue().
sold = queue.simulate_line(10, 1)   # Set var 'sold' assigned with var obj
                                    # queue and calling the function method
                                    # 'simulate_line' with params 10 secs
                                    # for till_show, and 1 sec for max_time.
print(sold) # Print out the persons where tickets are sold to.

