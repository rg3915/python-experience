#! /usr/bin/python3

from struct import unpack

# Read a binary file
with open('out.dat', 'rb') as f:
    content = f.read()
    print(content)
    print(unpack('hhh', content))
