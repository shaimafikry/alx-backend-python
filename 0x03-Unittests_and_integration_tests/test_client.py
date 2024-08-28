#!/usr/bin/env python3
""" testing"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """ class test"""
    # the func to be patched, the wanted return value
    @parameterized.expand([
        ("google", {"org": "res_org"}),
        ("abc", {"org": "res_org"})
    ])
    @patch('client.get_json', return_value={"org": "res_org"})
    def test_org(self, org_name, output, mock_obj):
        """ test org"""
        my_test = GithubOrgClient(org_name)
        # make the call
        self.assertEqual(my_test.org, output)
        # check if it was called more than once
        mock_obj.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
