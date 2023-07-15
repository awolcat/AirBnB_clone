#!/usr/bin/python3
"""Tests for State Class"""

from models import state
import unittest
State = state.State


class TestState(unittest.TestCase):
    """Unit tests for State class"""

    def test_city_doc(self):
        """Test state module and class documentation"""
        module_doc = state.__doc__
        class_doc = State.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_state(self):
        """Test State initialization"""
        new_state = State()
        new_state.name = 'Greater Accra'
        self.assertIsNotNone(new_state.id)
        self.assertIsNotNone(new_state.updated_at)
        self.assertIsNotNone(new_state.created_at)
        self.assertTrue(new_state.name == 'Greater Accra')
