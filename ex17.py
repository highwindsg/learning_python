from sys import argv
from os.path import exists

script, src_file, dst_file = argv

print(f"Copying from {src_file} to {dst_file}")

# we could do these two on one line, how?
in_file = open(src_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(dst_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(dst_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
