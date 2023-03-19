#Flask imports
from flask import Flask, render_template, send_file, make_response, url_for
from flask import Response

#Pandas 
import pandas as pd

import os
import io
import random

# Read the data 
df  = pd.read_csv("CO2.csv",error_bad_lines=False)

# Convert time format from unix milliseconds to datetime64 format
df['time'] = df['time'].astype('datetime64[ms]')


# Create a flask app
app = Flask(__name__)

# main route
@app.route('/')
@app.route('/pandas', methods=("POST", "GET"))
def GK():
    min_date = df['time'].min()
    max_date = df['time'].max()

    min_val = df['value'].min()
    max_val = df['value'].max()

    cwd = os.getcwd()
    with open(cwd + '/templates/home.html', 'a') as f:
        f.write(f"The duration of data is [{min_date} ~ {max_date} ]<br/>")
        f.write(f"The min CO2 values is: {min_val}<br/>")
        f.write(f"The max CO2 values is: {max_val}<br/>")

    return render_template('home.html',PageTitle = 'plot')
    #return render_template('home.html',PageTitle = "plot",table=[df.to_html(classes='data', index = False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=5000)

