#!/usr/bin/env python3

def add_multi_params(a, b, c, x=100, y=1000):
    """
    Below line will calculate the first 3 params
    and then including the optional two x and y params.
    """
    return a + b + c * x * y

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

result = add_multi_params(n1, n2, n3)   # Calculation will also include the
                                        # two optional parameters.
print(result)

