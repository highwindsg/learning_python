while True:
    line = input("> ")
    if line[0] == "#":  # 'line[0]' means the first item in the line or word.
        continue
    if line == "done":
        break
    print(line)
print("Done!")

# All the lines are printed except that starts with the hash '#' sign because
# when the 'continue' is executed, it ends the current iteration and jumps
# back to the while statement to start the next iteration, thus skipping the
# print statements.
