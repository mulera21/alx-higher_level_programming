#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < o:
    last_digit = -last_digit
    print("last digit {} is {} and {}".format(number, last_digit), end= "")
if last_digit > 5:
    print("and is greater than 5")

elif last_digit == 0:
    print("and is zero")

else:
    print("and is less than 6 and not 0")
