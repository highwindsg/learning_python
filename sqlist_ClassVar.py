#!/usr/bin/env python3

class Square():
    square_list = []

    def __init__(self, side1):
        self.side1 = side1
        self.square_list.append(self.side1)

    def print_sides(self):
        print("{} by {} by {} by {}".format(self.side1,
                                            self.side1,
                                            self.side1,
                                            self.side1)
            )

    # Overrode the repr magic method inherited from Object, and changed it to
    # return the Square object's side1.
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side1,
                                            self.side1,
                                            self.side1,
                                            self.side1)

sq1 = Square(5)
print(Square.square_list)
Square.print_sides(sq1)
print("using __repr__ method is", sq1)  # So when client calls for the printing
                                        # of sq1 in this case, instead of the obj
                                        # memory location is printed, side1 gets
                                        # to be printed instead.
