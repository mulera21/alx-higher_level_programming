#!/usr/bin/python3
"""
this module contain  function of addition 

"""

def add_integer(a, b=98):
	"""adds two intergers
	Args:
	a: first number
	b: second number

	Return:the sum of two numbers

	Raises:
	    TypeError: if a or b are not intergers/float numbers
	"""

	if not isinstance(a, (int, float)):
		raise TypeError("a must be an integer ")

	a = int(a)

	if not isinstance(b,(int, float)):
		raise TypeError("b must be an integer")

	b = int(b)

	return (a + b)

