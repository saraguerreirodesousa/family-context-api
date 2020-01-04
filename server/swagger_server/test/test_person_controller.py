# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.person import Person  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def test_get_person_by_id(self):
        """Test case for get_person_by_id

        Find person by ID
        """
        response = self.client.open(
            '/api/person/{personId}'.format(person_id='person_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
