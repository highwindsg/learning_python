def weapon_stash(num_knife, num_sword, num_gun, num_bomb):
    print(f"You have collected {num_knife} pieces of knives.")
    print(f"You also have {num_sword} long swords.")
    print(f"You also have {num_gun} short guns.")
    print(f"And finally you have {num_bomb} sets of bombs.")

print("We could just provide the number of weapon count directly.")
weapon_stash(5, 10, 7, 3)

print("Hey we found a second stash of weapons!")
stash2_knife = 4
stash2_sword = 12
stash2_gun = 10
stash2_bomb = 5
weapon_stash(stash2_knife, stash2_sword, stash2_gun, stash2_bomb)

print("Now the total number of each arsenal we have now are?")
weapon_stash(5 + 4, 10 + 12, 7 + 10, 3 + 5)

print("But still we can buy the weapons from a weapon shop, and the shop owner ask the below questions.")
num_knife = input("How many pieces of knives do you want to buy?: ")
num_sword = input("How many long swords do you want to buy?: ")
num_gun = input("How many short guns do you want to buy?: ")
num_bomb = input("How many sets of bombs do you want to buy?: ")
weapon_stash(num_knife, num_sword, num_gun, num_bomb)

