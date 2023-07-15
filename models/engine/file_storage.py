#!/usr/bin/python3
"""serializes instances to JSON file, deserializes JSON file to instances"""
import json


class FileStorage:
    """file storage creation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """saves objects to json file"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        """reloads"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State

        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():

                    if obj['__class__'] == 'BaseModel':
                        newObj = eval(obj['__class__'])(**obj)
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'User':
                        newObj = eval(obj['__class__'])(**obj)
                        user_attrs = obj.keys()
                        if 'email' in user_attrs:
                            newObj.email = obj['email']
                        if 'first_name' in user_attrs:
                            newObj.first_name = obj['first_name']
                        if 'last_name' in user_attrs:
                            newObj.last_name = obj['last_name']
                        if 'password' in user_attrs:
                            newObj.password = obj['password']
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'Place':
                        newObj = eval(obj['__class__'])(**obj)
                        place_attrs = obj.keys()
                        if 'city_id' in place_attrs:
                            newObj.city_id = obj['city_id']
                        if 'user_id' in place_attrs:
                            newObj.user_id = obj['user_id']
                        if 'name' in place_attrs:
                            newObj.name = obj['name']
                        if 'description' in place_attrs:
                            newObj.description = obj['description']
                        if 'number_rooms' in place_attrs:
                            newObj.number_rooms = obj['number_rooms']
                        if 'number_bathrooms' in place_attrs:
                            newObj.number_bathrooms = obj['number_bathrooms']
                        if 'max_guest' in place_attrs:
                            newObj.max_guest = obj['max_guest']
                        if 'price_by_night' in place_attrs:
                            newObj.price_by_night = obj['price_by_night']
                        if 'latitude' in place_attrs:
                            newObj.latitude = obj['latitude']
                        if 'longitude' in place_attrs:
                            newObj.longitude = obj['latitude']
                        if 'amenity_ids' in place_attrs:
                            newObj.amenity_ids = obj['amenity_ids'][:]
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'Amenity':
                        newObj = eval(obj['__class__'])(**obj)
                        amenity_attrs = obj.keys()
                        if 'name' in amenity_attrs:
                            newObj.name = obj['name']
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'City':
                        newObj = eval(obj['__class__'])(**obj)
                        city_attrs = obj.keys()
                        if 'name' in city_attrs:
                            newObj.name = obj['name']
                        if 'state_id' in city_attrs:
                            newObj.state_id = obj['state_id']
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'Review':
                        newObj = eval(obj['__class__'])(**obj)
                        review_attrs = obj.keys()
                        if 'place_id' in review_attrs:
                            newObj.place_id = obj['place_id']
                        if 'user_id' in review_attrs:
                            newObj.user_id = obj['user_id']
                        if 'text' in review_attrs:
                            newObj.text = obj['text']
                        self.__objects[key] = newObj

                    elif obj['__class__'] == 'State':
                        newObj = eval(obj['__class__'])(**obj)
                        state_attrs = obj.keys()
                        if 'name' in state_attrs:
                            newObj.name = obj['name']
                        self.__objects[key] = newObj

        except FileNotFoundError:
            pass
