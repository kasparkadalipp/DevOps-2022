#!/usr/bin/env python3
 
import connexion
from flask import Flask
from swagger_server import encoder
from flask_cors import CORS
 
def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    #app_name = Flask(__name__)
    #CORS(app_name)
    CORS(app.app)
    app.add_api('swagger.yaml', arguments={'title': 'Swagger IoT data'})
    app.run(port=8080)
 
 
if __name__ == '__main__':
    main()

