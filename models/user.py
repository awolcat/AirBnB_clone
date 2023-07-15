#!/usr/bin/python3
"""Module defines one class - User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that defines attributes specific to User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
