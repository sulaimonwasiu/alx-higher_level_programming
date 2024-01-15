#!/usr/bin/python3
"""Square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square Class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square Class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """Square Class
        """
        return self.width

    @size.setter
    def size(self, value):
        """Square Class
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Square Class
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Square Class
        """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
