#!/usr/bin/env python3
""" testing"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ testing"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """ test the func"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test the func"""
        # cm = context manager
        with self.assertRaises(KeyError) as cm:
            test = access_nested_map(nested_map, path)
            # key error 'b' -> path[-1]  == 'b'
            # cm.exception is the messageof the error
            self.assertEqual(cm.exception, path[-1])


if __name__ == '__main__':
    unittest.main()
