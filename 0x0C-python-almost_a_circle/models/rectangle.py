@@ -4,6 +4,7 @@
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
@@ -12,7 +13,7 @@ class Base:
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The active number of Base instances.
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0
@@ -36,7 +37,7 @@ def to_json_string(list_dictionaries):
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

@@ -48,12 +49,12 @@ def save_to_file(cls, list_objs):
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                f.write("")
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
@@ -76,9 +77,10 @@ def create(cls, **dictionary):
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        new = cls(7, 7)
        new.update(**dictionary)
        return new
        if dictionary and dictionary != {}:
            new = cls(7, 7, id="dummy")
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
@@ -92,8 +94,8 @@ def load_from_file(cls):
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
@@ -107,8 +109,8 @@ def save_to_file_csv(cls, list_objs):
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None:
                f.write("")
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
@@ -141,3 +143,44 @@ def load_from_file_csv(cls):
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
  10 changes: 8 additions & 2 deletions10  
0x0C-python-almost_a_circle/models/rectangle.py
 100644 → 100755
@@ -113,7 +113,10 @@ def update(self, *args, **kwargs):
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
@@ -127,7 +130,10 @@ def update(self, *args, **kwargs):
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
  14 changes: 10 additions & 4 deletions14  
0x0C-python-almost_a_circle/models/square.py
 100644 → 100755
@@ -44,7 +44,10 @@ def update(self, *args, **kwargs):
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
@@ -56,7 +59,10 @@ def update(self, *args, **kwargs):
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
@@ -75,5 +81,5 @@ def to_dictionary(self):

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} {}".format(self.id, self.x, self.y,
                                               self.width)
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
