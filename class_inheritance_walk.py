#!/usr/bin/env python3

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # Dog class will inherit the attrib of class Mammal.
    pass            # 'pass' is set in the body of the class so as not to be
                    # treated as an empty class.


class Cat(Mammal):  # Cat class inherit the attrib of class Mammal.
    def be_annoying(self):  # But also have it's own defined method 'be_annoying'
                            # with param self.
        print("annoying")


class Cow(Mammal):  # Cow class inherit the attrib of class Mammal.
    def milking(self):  # But also have it's own defined method 'milking' with
                        # param self.
        print("Producing milk")


class Goat(Mammal): # Goat class will inherit the attrib of class Mammal.
    pass            # 'pass' is set in the body of the class so as bot to be
                    # treated as an empty class.


dog1 = Dog()    # Set var dog1 to an instance of class Dog.
dog1.walk()     # From var dog1, get the walk method.

cat1 = Cat()    # Set var cat1 to an instance of class Cat.
cat1.be_annoying()  # From var cat1, get the be_annoying method.

cow = Cow()     # Set var cow to an instance of class Cow.
cow.milking()   # From var cow, get the milking method.

goat = Goat()   # Set var goat to an instance of class Goat.
goat.walk()     # From vr goat, get the walk method.

