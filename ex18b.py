def chicken_rice(*args):
    arg1, arg2, arg3, arg4 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}")

def mee_soto(arg1, arg2, arg3, arg4):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}")

def noodle(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")


chicken_rice("rice", "chicken", "cucumber", "chilli")
mee_soto("noodle", "soup", "chilli", "lemon")
noodle("meepok", "fishcake", "chilli")
