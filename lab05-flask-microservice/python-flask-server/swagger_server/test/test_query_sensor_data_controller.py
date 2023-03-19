# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQuerySensorDataController(BaseTestCase):
    """QuerySensorDataController integration test stubs"""

    def test_get_sensor_by_id(self):
        """Test case for get_sensor_by_id

        Find sensor data  by host
        """
        response = self.client.open(
            '/v2/sensor_data/{host}'.format(host=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getmaximum(self):
        """Test case for getmaximum

        Find maximum sensor data  by host
        """
        response = self.client.open(
            '/v2/maximum/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getminimum(self):
        """Test case for getminimum

        Find minimum sensor data  by host
        """
        response = self.client.open(
            '/v2/minimum/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
