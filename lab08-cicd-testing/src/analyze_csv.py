import pandas as pd 
import os 
import datetime

# tested on 13 digit input     
def convert_epoch_to_human_readable(epochTime):
    hr_date = datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%Y-%m-%d %H:%M:%S.%f')
    return hr_date
def get_year(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%Y')
def get_month(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%m')
def get_date(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%d')
def get_hour(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%H')
def get_minutes(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%M')
def get_seconds(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%S')
def get_miliseconds(epochTime):
    return datetime.datetime.utcfromtimestamp((epochTime/1000.0)).strftime('%f')

# argument: @filenmae: path to the file in string format, e.g. "./dehury/csv_data/co2.csv"
def read_csv(filename):
  df = pd.read_csv(filename)
  return df


# statement to read the csv file present in csv_data directory using read_csv function.
df = pd.read_csv(os.getcwd() + "/csv_data/CO2.csv")
print(df)

# Invoke the above convert_epoch_to_human_readable() function with a random epochTime, e.g. 1600763816518
print(convert_epoch_to_human_readable(1600763816518))

# Invoke above get_* functions with the epochTime 1600763816518.
print(get_year(1600763816518))
print(get_month(1600763816518))
print(get_date(1600763816518))
print(get_hour(1600763816518))
print(get_minutes(1600763816518))
print(get_seconds(1600763816518))
print(get_miliseconds(1600763816518))