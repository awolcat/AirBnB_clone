#!/usr/bin/python3
"""Tests for Place Class"""

from models import place
import unittest
Place = place.Place


class TestPlace(unittest.TestCase):
    """Unit tests for Place class"""

    def test_place_doc(self):
        """Test class and module documentation"""
        module_doc = place.__doc__
        class_doc = Place.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_place(self):
        """Test user initialization"""
        place = Place()
        place.name = 'The Place'
        place.description = 'Beach Apartments'
        place.number_rooms = 5
        place.max_guest = 6
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = [1, 2, 3, 4]
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.updated_at)
        self.assertIsNotNone(place.created_at)
        self.assertTrue(place.name == 'The Place')
        self.assertTrue(place.description == 'Beach Apartments')
        self.assertTrue(place.max_guest == 6)
        self.assertTrue(place.latitude == 0.0)
