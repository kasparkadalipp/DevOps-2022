import connexion
import six
from flask import jsonify

from swagger_server import util
import json
import pandas as pd


def get_sensor_by_id(host):  # noqa: E501

    try:
        df = pd.read_csv("/tmp/iot.csv")
        if host in df['host'].values :
            df_host = df.loc[df['host'] == host]
            data = df_host.to_json(orient="records")

            status = 200
            #data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            message = {"Error message": "Invalid device"}
            data = json.dumps(message)
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status

def getmaximum(sensor):  # noqa: E501
    """Find maximum sensor data  by ID

    Returns a list of sensor data # noqa: E501

    :param sensor: Device id to search in the data
    :type sensor: str

    :rtype: Device
    """
    try:
        host = int(sensor)
        df = pd.read_csv("/tmp/iot.csv")
        if host in df['host'].values :
            df_host = df.iloc[[df.value.idxmax()], :]
            data = df_host.to_json(orient="records")

            status = 200
            #data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            message = {"Error message": "Invalid device"}
            data = json.dumps(message)
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status


def getminimum(sensor):  # noqa: E501
    """Find minimum sensor data  by ID

    Returns a list of sensor data # noqa: E501
    :param sensor: Device id to search in the data
    :type sensor: str

    :rtype: Device
    """
    try:
        host = int(sensor)
        df = pd.read_csv("/tmp/iot.csv")
        if host in df['host'].values :
            df_host = df.iloc[[df.value.idxmin()], :]
            data = df_host.to_json(orient="records")

            status = 200
            #data = {"Success message": "Device deleted from the csv"}
        else:
            status = 400
            message = {"Error message": "Invalid device"}
            data = json.dumps(message)
    except Exception as e:
            data = {"Error message": str(e)}
            status = 400
    return json.loads(data),status
