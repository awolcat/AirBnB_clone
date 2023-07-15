#!/usr/bin/python3
"""This module defines the BaseModel class"""

from uuid import uuid4
import datetime
from models import storage


class BaseModel():
    """This class defines all the common attributes for different
    classes in the AirBnB project.
    These are:
        id - a unique identification number
        created_at - the date and time the object is created
        updated_at - the last date and time the object was updated
    """
    """BaseModel also defines methods that are universal to all classes
    in the AirBnB project
    These are:
        save(self) - updates the updated_at attribute with current time
        to_dict(self) - returns a dictionary with all attributes of the object
                        i.e., keys and values of __dict__
    """

    def __init__(self, *args, **kwargs):
        """Object instantiation method:
        arguments:
            can be nil or keyword arguments
        Return:
            None
        """
        if kwargs and len(kwargs) >= 1:
            for key, value in kwargs.items():
                if key == 'name':
                    self.name = value
                if key == 'my_number':
                    self.my_number = value
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                if key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            # Optionally remove this line and use ifs in to_dict()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of BaseModel object
        arguments:
            nil
        Return:
            a string representation of BaseModel object
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update updated_at attribute with the current date and time
        arguments:
            nil
        Return:
            nil
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Create a dictionary representation of an object
        arguments:
            nil
        Return:
            A dictionary object with all attributes of
            a given instance
        """
        my_dict = self.__dict__.copy()
        #if isinstance(my_dict['created_at'], datetime.datetime):
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        #if isinstance(my_dict['updated_at'], datetime.datetime):
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
