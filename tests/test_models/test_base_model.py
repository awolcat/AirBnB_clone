#!/usr/bin/python3
"""Test Module for BaseModel Class"""

import unittest
import datetime
from models import base_model

BaseModel = base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    """Unit Testing for BaseModel class"""

    def test_documentation(self):
        """Test module, class, and method documentation"""
        module_doc = base_model.__doc__
        class_doc = BaseModel.__doc__
        init_doc = BaseModel.__init__.__doc__
        str_doc = BaseModel.__str__.__doc__
        save_doc = BaseModel.save.__doc__
        dict_doc = BaseModel.to_dict.__doc__
        self.assertTrue(len(module_doc) > 0)
        self.assertTrue(len(class_doc) > 0)
        self.assertTrue(len(init_doc) > 0)
        self.assertTrue(len(str_doc) > 0)
        self.assertTrue(len(save_doc) > 0)
        self.assertTrue(len(dict_doc) > 0)

    def test_init(self):
        """Test cases for BaseModel.__init__()""" 
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        self.assertIsInstance(obj.id, str)

    def test_str(self):
        """Test str magic method"""
        obj = BaseModel()
        self.assertTrue(str(obj), str)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        updated_at = obj.updated_at
        obj.save()
        updated_at_2 = obj.updated_at
        self.assertTrue(updated_at < updated_at_2)

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        objDict = obj.to_dict()
        self.assertIsInstance(objDict, dict)
        self.assertIsInstance(objDict['updated_at'], str)
        self.assertIsInstance(objDict['created_at'], str)
        self.assertIsInstance(objDict['id'], str)
        self.assertEqual(objDict['__class__'], "BaseModel")

