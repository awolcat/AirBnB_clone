#!/usr/bin/python3
"""Class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that defines attributes specific to City"""
    state_id = ""  # It will be the state.id
    name = ""
