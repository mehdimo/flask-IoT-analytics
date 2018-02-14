import numpy as np
import pandas
from pandas import DataFrame
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def chart():
    df = pandas.read_csv('data/data.csv')
    days = np.unique(df['day'])

    allValues = {}
    for day in days:
        df_ = df.query('day==' + str(day))
        labels = df_['hour']
        print labels
        values_dewp = df_['DEWP']
        values_temp = df_['TEMP']
        values1 = [values_dewp, values_temp, labels]
        allValues[day] = values1
    return render_template('charts.html', days = days, values=allValues)

if __name__ == "__main__":
    app.run()
