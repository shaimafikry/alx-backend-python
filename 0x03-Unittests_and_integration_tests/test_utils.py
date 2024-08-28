#!/usr/bin/env python3
""" testing"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


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


class TestGetJson(unittest.TestCase):
    """ testing mocing"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, input, output):
        """ mocing test"""
        # applay patch on any call to requests.get
        with patch('requests.get') as res:
            # add the mocked output
            res.return_value.json.return_value = output
            self.assertEqual(get_json(input), output)
            # to make sure its called once
            res.assert_called_once_with(input)


class TestMemoize(unittest.TestCase):
    """ test memoize"""
    def test_memoize(self):
        """ test memoize"""
        class TestClass:
            """ class teseted"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as cm:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            cm.assert_called_once()


if __name__ == '__main__':
    unittest.main()
