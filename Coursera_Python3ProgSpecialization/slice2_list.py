#!/usr/bin/env python3

"""
List Slices
===========
The slice operation we saw with strings also work on lists. 
Remember that the first index is the starting point for the 
slice and the second number is one index past the end of the 
slice (up to but not including that element). 
Recall also that if you omit the first index 
(before the colon), the slice starts at the beginning of the 
sequence. If you omit the second index, the slice goes to the 
end of the sequence.
"""

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])
print("")

# ref: https://fopp.umsi.education/books/published/fopp/Sequences/TheSliceOperator.html
