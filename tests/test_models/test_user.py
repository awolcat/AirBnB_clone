#!/usr/bin/python3
"""Tests for User Class"""

from models import user
from models.base_model import BaseModel
import unittest
import datetime
User = user.User


class TestUser(unittest.TestCase):
    """Unit tests for User class"""

    def test_user_doc(self):
        """Test user class and module documentation"""
        module_doc = user.__doc__
        class_doc = User.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_user(self):
        """Test user initialization"""
        user_1 = User()
        user_1.first_name = 'Jo'
        user_1.last_name = 'Shmo'
        user_1.email = 'shmo@mail.com'
        user_1.password = 'RoOt'
        self.assertIsInstance(user_1, BaseModel)
        self.assertIsNotNone(user_1.id)
        self.assertIsNotNone(user_1.updated_at)
        self.assertIsNotNone(user_1.created_at)
        self.assertIsInstance(user_1.id, str)
        self.assertIsInstance(user_1.updated_at, datetime.datetime)
        self.assertIsInstance(user_1.created_at, datetime.datetime)
        self.assertTrue(user_1.first_name == 'Jo')
        self.assertTrue(user_1.last_name == 'Shmo')
        self.assertTrue(user_1.email == 'shmo@mail.com')
        self.assertTrue(user_1.password == 'RoOt')
        self.assertIsNotNone(user_1.first_name)
        self.assertIsNotNone(user_1.last_name)
        self.assertIsNotNone(user_1.email)
        self.assertIsNotNone(user_1.password)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
