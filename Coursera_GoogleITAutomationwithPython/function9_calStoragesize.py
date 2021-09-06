#!/usr/bin/env python3

"""
Question 5
If a filesystem has a block size of 4096 bytes, this means that a file comprised of 
only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes 
will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in 
the calculate_storage function below, which calculates the total number of bytes 
needed to store a file of a given size?
"""

def calculate_storage(filesize):
    block_size = 4096
    
    # Use floor division (eg. //) to calculate how many blocks are fully occupied.
    full_blocks = filesize // block_size
    
    # Use the modulo operator (eg. %) to check whether there's any remainder.
    partial_block_remainder = filesize % block_size
    
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0: # if there is a remainder from modulo in line 18.
        return block_size * (full_blocks + 1)
    return full_blocks * block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
print("")