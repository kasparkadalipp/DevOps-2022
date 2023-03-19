import connexion
import six
from flask import jsonify
from swagger_server import util
import pandas as pd
import json


from swagger_server import util


def upload_post(upfile):  # noqa: E501

	df = pd.read_csv(upfile)
	df.to_csv("/tmp/iot.csv")
	data = {"message": "File Successfully uploaded"}

	return data, 200

