# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModifySensorDataController(BaseTestCase):
    """ModifySensorDataController integration test stubs"""

    def test_update_sensor_data(self):
        """Test case for update_sensor_data

        Updated Sensor name
        """
        body = Device()
        response = self.client.open(
            '/v2/modify',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
