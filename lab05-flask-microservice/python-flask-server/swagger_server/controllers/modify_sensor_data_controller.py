import connexion
import six
from flask import jsonify

from swagger_server import util
import json
import pandas as pd


def update_sensor_data(body):  # noqa: E501
    """Updated Sensor name

    # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """

        # noqa: E501
    try:
        body = connexion.request.get_json()

        host = body['host']
        unit = body['unit']

        df = pd.read_csv("/tmp/iot.csv")
        if host in df['host'].values :
            df.loc[df['host'] == host, 'unit'] = unit
            status = 200
            data = {"Success message": "CSV updated and saved as iot_updated_modifed.csv in /tmp"}
            df.to_csv("/tmp/iot.csv")   
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
 
    return data, status
