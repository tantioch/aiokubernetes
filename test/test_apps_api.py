# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import aiokubernetes
from aiokubernetes.api.apps_api import AppsApi  # noqa: E501
from aiokubernetes.rest import ApiException


class TestAppsApi(unittest.TestCase):
    """AppsApi unit test stubs"""

    def setUp(self):
        self.api = aiokubernetes.api.apps_api.AppsApi(None)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
