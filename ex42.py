## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## A class named Dog that is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## From self, get the attribute of name and set it to name.
        self.name = name

## A class named Cat that is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## From self, get the attribute name and set it to name.
        self.name = name

## A class named Person is-a object.
class Person(object):

    def __init__(self, name):
        ## From self, get the name attribute, and set it to name.
        self.name = name

        ## From self, get the self attribute, and set it to None.
        self.pet = None

## A class named Employee is-a Person.
class Employee(Person):

    def __init_(self, name, salary):
        ## A function named super has the self and Employee params, has a init with params name.
        super(Employee, self).__init__(name)
        ## From self, get the salary attribute and set it to salary.
        self.salary = salary

## A class named Fish is-a object.
class Fish(object):
    pass

## A class named Salmon that is-a Fish.
class Salmon(Fish):
    pass

## A class named Halibut that is-a Fish.
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary, get the pet attribute, and set it to satan.
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank")

## from frank, get the pet attribute, and set it to rover.
frank.pet = rover

## Set flipper to an instance of class Fish.
flipper = Fish()

## Set crouse to an instance of class Salmon.
crouse = Salmon()

## set harry to an instance of class Halibut.
harry = Halibut()
