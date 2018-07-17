from sys import argv

script, booktitle = argv

txt = open(booktitle)
print(f"This is your favourite {booktitle}:")
print(txt.read())

print("Read the book again:")
booktitle_again = input("> ")
txt_again = open(booktitle_again)
print(txt_again.read())

txt.close()
txt_again.close()
