#! /usr/bin/python3

from struct import pack

binary = [1000, 1024, 2048]

# Write a binary file
with open('out.dat', 'wb') as f:
    for b in binary:
        f.write(pack('h', b))
