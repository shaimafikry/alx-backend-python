#!/usr/bin/env python3
""" testing"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
from fixtures import (
      org_payload,
      repos_payload,
      expected_repos,
      apache2_repos
)


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

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, property_mocked_obj):
        """ test that a method calls a property"""
        # make the default value
        property_mocked_obj.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        # create new instance
        my_test = GithubOrgClient('google')
        # call the proberty
        my_res = my_test._public_repos_url
        self.assertEqual(my_res, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        " test puplic repos"
        # Define a mock return value for the get_json calls
        mock_repos = [{"name": "repo1", "license": {"key": "lic1"}}]
        mock_get_json.return_value = mock_repos
        url = "https://api.github.com/orgs/google/repos"
        # Mock the _public_repos_url property
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mck_r_url:
            mck_r_url.return_value = url

            # Create an instance of the client
            client = GithubOrgClient('google')

            # Call the public_repos method
            result = client.public_repos()

            # Check if the method returns the expected repository names
            expected_repos = ["repo1"]
            self.assertEqual(result, expected_repos)

            # Assert that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(url)

            # Assert that the _public_repos_url was accessed once
            mck_r_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, output):
        """ test has_licence"""
        self.assertEqual(GithubOrgClient.has_license
                         (repo, license_key), output)

@parameterized_class([
    {'org_payload': org_payload,
     'repos_payload': repos_payload,
     'expected_repos': expected_repos,
     'apache2_repos': apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ test integration"""
    @classmethod
    def setUpClass(cls):
        """ class method to setup for the tests"""
        cls.get_patcher = patch('requests.get')
        # starts the patcher and assigns the mock object to mock_get
        cls.mock_get  = cls.get_patcher.start()
        # side_effect used when there is more than one value returned on different calls
        def mock_get_side_effect(url, *args, **kwargs):
            if url.endswith('/orgs/some-org'):
                return unittest.mock.Mock(json=lambda: cls.org_payload)
            elif url.endswith('/orgs/some-org/repos'):
                return unittest.mock.Mock(json=lambda: cls.repos_payload)
            elif url.endswith('/repos/some-org/some-repo'):
                return unittest.mock.Mock(json=lambda: cls.apache2_repos)
            else:
                raise ValueError("Unexpected URL")


        cls.mock_get.side_effect = mock_get_side_effect

    @classmethod
    def tearDownClass(cls):
        """ delete all after finishing"""
        # cls.get_patcher.stop() stops the patcher, restoring requests.get to its original state.
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test methods"""
        client = GithubOrgClient('google')
        result = client.public_repos()
        self.assertEquals(result, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
