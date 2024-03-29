#!/usr/bin/python3
"""Base Class
"""


class Base:
    """Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_nb_objects(cls):
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        import json
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation of json_string"""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """JSON string representation of dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """JSON string representation of load_from_file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                r = [cls.create(**d) for d in cls.from_json_string(f.read())]
                return r
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        import csv
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for o in list_objs:
                writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """JSON string representation of load_from_file"""
        import csv
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fieldnames)
                instances = []
                for row in reader:
                    dict_ = {key: int(value) for key, value in row.items()}
                    instance = cls.create(**dict_)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
