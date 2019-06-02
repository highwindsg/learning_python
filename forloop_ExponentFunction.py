#!/usr/bin/env python3

# Create function 'raise_to_power' with two params.
def raise_to_power(base_num, power_num):
    result = 1  # Set var obj 'result' to 1
    for index in range(power_num):
        result = result * base_num
    return result


# Client call the function of 'raise_to_power()' with params 3 and 4, and then
# print out the result.
print(raise_to_power(3, 4)) # Read as 3 to the power of 4, eg. 3^4
