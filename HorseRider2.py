#!/usr/bin/env python3
"""
Create a class called Horse and a class called Rider. User composition to model
a horse that has-a rider.
"""
class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse


# The var harry_the_horse is assigned with the Horse obj that has the name "Harry"
# as the param.
harry_the_horse = Horse("Harry")
# The var the_rider is assigned with the Rider obj that has the rider's name and
# horse param that is assigned to another var harry_the_horse.
the_rider = Rider("Sally", harry_the_horse)

# From the_rider var, which has been assigned the Rider obj params, get the horse
# param, which has been assigned to var harry_the_horse, that has the Horse obj
# with param "Harry".
print(the_rider.horse.name)

