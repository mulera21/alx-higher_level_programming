#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings representing the attributes and methods of the object.

    Example:
        class MyClass:
            def __init__(self):
                self.my_attribute = 42

            def my_method(self):
                return "Hello, world!"

        obj = MyClass()
        result = lookup(obj)
        print(result)

    Output:
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attribute', 'my_method']
    """
    return dir(obj)
