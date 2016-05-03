#! /usr/bin/python3

import struct

binary = [1, 2, 3, 4, 1024, 2048]

print('Original binary:', binary)
print('\nshort:')
for b in binary:
    print(struct.pack('h', b))

print('\nlong:')
for b in binary:
    print(struct.pack('l', b))
