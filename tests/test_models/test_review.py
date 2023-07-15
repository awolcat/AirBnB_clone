#!/usr/bin/python3
"""Tests for Review Class"""

from models import review
import unittest
Review = review.Review


class TestReview(unittest.TestCase):
    """Unit tests for Review class"""

    def test_review_doc(self):
        """Test review module and class documentation"""
        module_doc = review.__doc__
        class_doc = Review.__doc__
        self.assertTrue(len(module_doc) > 1)
        self.assertTrue(len(class_doc) > 1)

    def test_review(self):
        """Test review initialization"""
        my_review = Review()
        self.assertIsNotNone(my_review.id)
        self.assertIsNotNone(my_review.updated_at)
        self.assertIsNotNone(my_review.created_at)
