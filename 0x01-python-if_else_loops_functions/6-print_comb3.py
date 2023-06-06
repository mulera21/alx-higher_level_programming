#!/usr/bin/python3

for letters in range(10):
    for num in range(letters+1, 10):
        print("{:02d},".format(letters*10+num), end=" ")
print()
