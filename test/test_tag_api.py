# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kimai_python
from kimai_python.api.tag_api import TagApi  # noqa: E501
from kimai_python.rest import ApiException


class TestTagApi(unittest.TestCase):
    """TagApi unit test stubs"""

    def setUp(self):
        self.api = kimai_python.api.tag_api.TagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_tags_get(self):
        """Test case for api_tags_get

        Fetch all existing tags  # noqa: E501
        """
        pass

    def test_api_tags_id_delete(self):
        """Test case for api_tags_id_delete

        Delete a tag  # noqa: E501
        """
        pass

    def test_api_tags_post(self):
        """Test case for api_tags_post

        Creates a new tag  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
