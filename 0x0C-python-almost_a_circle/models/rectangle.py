#!/usr/bin/python3
"""Module models.rectangle with rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base class
        private attrs: width, height, x, y
        all have getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instanciates width, height, x, y, and id
            first 4 attributes all have getter and setter methods
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """Checks if value is an int
            name: name of value
            value: value to check if int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """prints the rectangle with '#' """
        if self.y != 0:
            for i in range(self.y):
                print()
        for i in range(self.height):
            num_space = self.x * ' '
            print("{}".format(num_space), end="")
            for j in range(self.width):
                print("", end="#")
            print()

    def update(self, *args, **kwargs):
        """updates the current attributes with given values"""
        count = 0
        for i in args:
            if count == 0:
                self.id = i
            elif count == 1:
                self.width = i
            elif count == 2:
                self.height = i
            elif count == 3:
                self.x = i
            else:
                self.y = i
            count += 1
        if args:
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """Function to turn self into a dictionary"""
        new_dict = {'x': self.x, 'y': self.y, 'id': self.id}
        new_dict['height'], new_dict['width'] = self.height, self.width
        return new_dict

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def __str__(self):
        """string representation of rectangle object"""
        string = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        string += " - {}/{}".format(self.width, self.height)
        return string
