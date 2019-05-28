#/usr/bin/env python3

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


#say_hi("Mike", 35)
#say_hi("Steve", 70)

name = input("Please enter your name: ")
age = input("And enter your age: ")

say_hi(name, age)

