#!/usr/bin/env python3


def sum_items(list1, list2):
    """ (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >> sum_items([1, 2, 3], [2, 4, 2])
    [3, 5, 5]
    """

    sum_list = []   # Start var sum_list with an empty list first.

    # To ensure that range takes into consideration the length of list1.
    for i in range(len(list1)):
        # Then add the index position of list1 with index position of list2,
        # and append it to var sum_list.
        sum_list.append(list1[i] + list2[i])

    return sum_list     # Return the appended list to the function name.


# Func call sum_items() with two params of two different lists.
Ans = sum_items([1, 2, 3], [2, 4, 2])
print(Ans)

