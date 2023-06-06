#!/usr/bin/python3

for letters in range(0, 100):
    print("{:02d}".format(letters), end=', ' if letters < 99 else "\n")
