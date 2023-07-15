#!/usr/bin/python3
"""Tests for City Class"""

from models import city
import unittest
City = city.City


class TestCity(unittest.TestCase):
    """Unit tests for City class"""

    def test_city_doc(self):
        """Test city module and class documentation"""
        module_doc = city.__doc__
        class_doc = City.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_city(self):
        """Test user initialization"""
        city = City()
        city.name = 'Accra'
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.updated_at)
        self.assertIsNotNone(city.created_at)
        self.assertTrue(city.name == 'Accra')
