import pandas as pd
from influxdb import InfluxDBClient
import sys
import os

# get $INFLUX_DB_NAME and $CSV_FILENAME from the environment variables
client = InfluxDBClient(host=os.getenv('INFLUX_DB_HOST') , port=8086)
dbname = os.getenv('INFLUX_DB_NAME')
# Check for existing data base
client.drop_database(dbname)
client.create_database(dbname)
client.switch_database(dbname)

csvReader = pd.read_csv('./flask-frontend/' + os.getenv('CSV_FILENAME'))

for row_index, row in csvReader.iterrows() :
	tags = row[3]
	json_body = [{
	"measurement": row[0],
	"time": row[2],
	"tags": {
    	"host": tags
	},
	"fields": {
    	"unit": row[4],
    	"value": row[5],
  	}
	}]
	print(json_body)
	client.write_points(json_body)