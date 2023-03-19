# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDeleteSensorDataController(BaseTestCase):
    """DeleteSensorDataController integration test stubs"""

    def test_delete_sensor_data(self):
        """Test case for delete_sensor_data

        Delete sensor data
        """
        response = self.client.open(
            '/v2/sensor_data/{host}'.format(host=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
