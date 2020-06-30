#!/usr/bin/python3
""" Base module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class Model
    """
    def __init__(self, *args, **kwargs):
        """ Constructor
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String Literal
        """
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return (mssg)

    def help_add(self):
        print('add two integral numbers')

    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary.
        """
        tdic = {}
        tdic["__class__"] = type(self).__name__
        for i, j in self.__dict__.items():
            if isinstance(j, datetime):
                tdic[i] = j.isoformat()
            else:
                tdic[i] = j
        return (tdic)
