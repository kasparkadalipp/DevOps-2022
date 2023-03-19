import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import sys
import numpy as np
import time
# 1. Read data from influxdb running deployment VM
local_influxdb_name = sys.argv[1]
local_influxdb_host = sys.argv[2]
print(local_influxdb_name,local_influxdb_host)
# client to extract data from data_source
data_sink = InfluxDBClient(
	host=local_influxdb_host,
	port=8086
)
data_sink.switch_database(local_influxdb_name)

query = "select * from preprocessed"
df = pd.DataFrame(data_sink.query(query).get_points())
df["time"] = pd.to_datetime(df["time"], errors="coerce")

# 2. Make the clusters 
session=pd.cut(df.time.dt.hour,
           	[0,6,12,18,23],
           	labels=["Night","Morning","Afternoon","Evening"],
           	include_lowest=True)

df['time_interval'] =session
df['time_interval'] = df['time_interval'].astype(str)

# df["time"] = pd.to_datetime(df["time"], errors="coerce")
# df = df.set_index('time')

#3. Insert the data frame to Influxdb running in deployment VM

data_client = DataFrameClient(
	host=local_influxdb_host,
	port=8086
)

dbname = 'cluster'

data_client.drop_database(dbname)
data_client.create_database(dbname)
data_client.switch_database(dbname)

# Code for inserting
for group,dataframe in df.groupby(["time_interval"]):
	for host, df_ in dataframe.groupby(["host"]):
		df_ = df_.reset_index()
		tags = {"time_interval": group,"host":host}
		fields = df_[["time","pm1_0", "pm2_5", "pm10"]]
		fields = fields.set_index("time")
		data_client.write_points(fields, 'cluster', tags, protocol="line")
		time.sleep(1)