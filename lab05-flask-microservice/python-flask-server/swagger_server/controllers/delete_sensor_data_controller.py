import connexion
import six
from flask import jsonify
import json
import pandas as pd


def delete_sensor_data(host):  # noqa: E501
    """Delete sensor data

    This can only be done by the logged in user. # noqa: E501

    :param host: Sensor Id that need to be updated
    :type host: int

    :rtype: None
    """
    try:
        df = pd.read_csv("/tmp/iot.csv")
        if host in df['host'].values :
            indexNames = df[ df['host'] == host].index
            df.drop(indexNames , inplace=True)
            df.to_csv("/tmp/iot.csv")
            status = 200
            data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            data = {"Error message": "Invalid device"}
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return jsonify(data),status
