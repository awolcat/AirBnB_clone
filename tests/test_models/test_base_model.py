#!/usr/bin/python3
"""Test Module for BaseModel Class"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Unit Testing for BaseModel class"""

    def test_init(self):
        """Test cases for BaseModel.__init__()"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertIsInstance(obj.id, str)

