#!/usr/bin/python3
"""Class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that defines attributes specific to amenities"""
    name = ""
