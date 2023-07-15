#!/usr/bin/python3
"""Class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that defines attributes specific to Review"""
    place_id = ""  # Will be the Place.id
    user_id = ""  # Will be the user.id
    text = ""
