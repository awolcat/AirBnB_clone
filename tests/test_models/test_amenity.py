#!/usr/bin/python3
"""Tests for Amenity Class"""

from models import amenity
import unittest
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity class"""

    def test_amenity_doc(self):
        """Test amenity module and class documentation"""
        module_doc = amenity.__doc__
        class_doc = Amenity.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_amenity(self):
        """Test Amenity initialization"""
        amenity = Amenity()
        amenity.name = 'Lift'
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsNotNone(amenity.created_at)
        self.assertTrue(amenity.name == 'Lift')
