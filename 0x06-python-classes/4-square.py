#!/usr/bin/python3

class Square:

    def __init__(self, size):
         self.size = size
    
    def size(self):
         return self.size
    
    def size(self, value):
         if not isinstance(value, int):
              raise TypeError("size must be interger")
         elif value < 0:
              raise ValueError("size must be >=0")
         else:
              self.size = value
    def area(self):
         return self.size ** 2