#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import os
import pep8
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setUp(self):
        """Setup the TestConsole"""

        self.console = HBNBCommand()

    def tearDown(self):
        """Cleanup after the tests run"""

        self.console.do_quit(None)

    def test_pep8(self):
        """Check for PEP8"""

        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py', 'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 Error")

    def test_create(self):
        """Test creating an instance"""

        self.console.do_create("BaseModel name='test'")
        key = "BaseModel.test"
        obj = storage.all().get(key)
        self.assertIsNotNone(obj)

    def test_show(self):
        """Test displaying an object"""

        self.console.do_create("BaseModel name='test'")
        key = "BaseModel.test"
        obj = storage.all().get(key)
        output = self.console.do_show("BaseModel test")
        self.assertIn(str(obj), output)

    def test_destroy(self):
        """Test destroying an object"""

        self.console.do_create("BaseModel name='test'")
        key = "BaseModel.test"
        obj = storage.all().get(key)
        self.console.do_destroy("BaseModel test")
        self.assertNotIn(key, storage.all().keys())

    def test_all(self):
        """Test displaying all objects"""

        self.console.do_create("BaseModel name='test1'")
        self.console.do_create("BaseModel name='test2'")
        output = self.console.do_all("BaseModel")
        self.assertIn("test1", output)
        self.assertIn("test2", output)

    def test_update(self):
        """Test updating an object"""

        self.console.do_create("BaseModel name='test'")
        key = "BaseModel.test"
        self.console.do_update("BaseModel test name 'test2'")
        obj = storage.all().get(key)
        self.assertEqual(obj.name, "test2")

    def test_count(self):
        """Test counting the number of objects"""

        self.console.do_create("BaseModel name='test1'")
        self.console.do_create("BaseModel name='test2'")
        output = self.console.do_count("BaseModel")
        self.assertEqual(output, 2)

if __name__ == '__main__':
    unittest.main()
