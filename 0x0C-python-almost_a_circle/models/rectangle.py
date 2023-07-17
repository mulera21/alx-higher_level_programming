#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    
    @property
    def width(self):
         """Getter for width attribute."""
         return self.__width  
    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if type(value) != int:
            raise TypeError("width must be interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
         """Getter for height attribute."""
         return self.__height
      
    @height.setter
    def height(self, value):
        """Setter for width attribute."""
        if type(value) != int:
            raise TypeError("height must be interger")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
         """Getter for x attribute"""
         return self.__x 
    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
         """Getter for y attribute."""
         return self.__y 
      
    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height
    def display(self):
        """display the '#' character"""
        for  _ in range(self.y):
            print()

        for _ in range(self.height):
            print("#" * self.width)
    
    def update(self, *args, **kwargs):
           """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
           if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            elif kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        
    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
     