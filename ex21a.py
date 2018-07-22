def addition(num1, num2):
    print(f"Addition {num1} + {num2}")
    return num1 + num2

def subtraction(num1, num2):
    print(f"Subtraction {num1} - {num2}")
    return num1 - num2

def multiplication(num1, num2):
    print(f"Multiplication {num1} * {num2}")
    return num1 * num2

def division(num1, num2):
    print(f"Division {num1} / {num2}")
    return num1 / num2

print("Let's do some mathmatical calculations with funcitons!")

age = addition(40, 5)
height = subtraction(200,22)
weight = multiplication(5,3)
iq = division(160,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Below is just to add it all up anyway.
print("Just to add it all together for fun.")

ans = addition(age, subtraction(height, multiplication(weight, division(iq, 2))))

print("So we have: ", ans, "can you calculate mentally")

