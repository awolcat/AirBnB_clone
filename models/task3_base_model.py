#!/usr/bin/python3

from uuid import uuid4
import datetime

"""This module defines the class BaseModel,
    which defines all the common attributes
    of the different classes in the AirBnB clone
"""


class BaseModel():
    """This class defines all the common attributes for different
        classes in the AirBnB project.
        These are:
            id - a unique identification number
            crreated_at - the date and time the object is created
            updated_at - the last date and time the object was updated
        
        BaseModel also defines methods that are universal to all classes
        in the AirBnB project
        These are:
            save(self) - updates the updated_at attribute with current time
            to_dict(self) - returns a dictionary with all attributes of the object
                            ie, keys and values of __dict__
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """This method defines and returns a string representation
            of an instance of the BaseModel class or its children
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the public instance attribute updated_at
            with the current date and time
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Create a dictionary representation of an object
            Return: A dictionary object with all attributes of
                    a given instance
        """
        my_dict = self.__dict__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
