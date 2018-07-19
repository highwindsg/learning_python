def elephant_food(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

def elephant_food_together(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg2: {arg3}")

def elephant_eats_one(arg1):
    print(f"arg1: {arg1}")

def elephant_eats_none():
    print("Elephant eats nothing.")


elephant_food("apple", "peanuts", "watermelon")
elephant_food_together("apple", "peanuts", "watermelon")
elephant_eats_one("peanuts!!")
elephant_eats_none()

