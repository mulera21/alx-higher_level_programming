#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10

b = 5

results_add = add(a, b)
results_sub = sub(a, b)
results_mul = mul(a, b)
results_div = div(a, b)

print("{} + {} = {}".format(a, b, results_add))
print("{} - {} = {}".format(a, b, results_sub))
print("{} * {} = {}".format(a, b, results_mul))
print("{} / {} = {}".format(a, b, results_div))

