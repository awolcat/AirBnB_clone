#!/usr/bin/python3
"""Tests for User Class"""

from models import user
import unittest
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
        self.assertIsNotNone(user_1.id)
        self.assertIsNotNone(user_1.updated_at)
        self.assertIsNotNone(user_1.created_at)
        self.assertTrue(user_1.first_name == 'Jo')
        self.assertTrue(user_1.last_name == 'Shmo')
        self.assertTrue(user_1.email == 'shmo@mail.com')
        self.assertTrue(user_1.password == 'RoOt')
