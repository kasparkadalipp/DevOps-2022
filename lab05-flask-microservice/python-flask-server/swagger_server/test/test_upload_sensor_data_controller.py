# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestUploadSensorDataController(BaseTestCase):
    """UploadSensorDataController integration test stubs"""

    def test_upload_post(self):
        """Test case for upload_post

        Uploads a file.
        """
        data = dict(upfile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/v2/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
