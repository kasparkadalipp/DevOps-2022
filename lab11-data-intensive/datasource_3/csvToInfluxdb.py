import pandas as pd
from influxdb import InfluxDBClient
import os
import glob
import sys

#dbname = sys.argv[1]

dbname = "datasource_3"
client = InfluxDBClient(host='172.17.91.48', port=8087)

# Check for existing database
client.drop_database(dbname)
client.create_database(dbname)
client.switch_database(dbname)

#filename = sys.argv[2]
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

for f in csv_files:
        print('Inserted data from',f)
#       file_path = open(filename,'r')
        csvReader = pd.read_csv(f)
        data = []
        for row_index, row in csvReader.iterrows() :
                tags = row[3]
                json_body = {
                "measurement": "air_quality",
                "time": row[2],
                "tags": {
                        "host": tags
                        },
                "fields": {
                        "lat":row[4],
                        "long": row[5],
                        "pm1_0": row[6],
                        "pm2_5": row[7],
                        "pm10" : row[8]
                                }
                        }
                data.append(json_body)
        client.write_points(data)
print("Data inserted successfully")
