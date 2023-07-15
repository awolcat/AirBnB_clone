#!/usr/bin/python3
"""Module defines one class - User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
