#!/usr/bin/python3

for letters in range(ord('a'), ord('z')+1):
    if chr(letters) not in ['q', 'e']:
        print("{:c}".format(letters), end=' ')
