import plotly_express as px
import pandas as pd 
import numpy as np
import csv

def plotfigure (datapath):
    with open(datapath) as csv_file:
        read= pd.read_csv(csv_file)
    graph= px.scatter(read, x= 'Coffee in ml' , y = 'sleep in hours')
    graph.show()

def getdatasource(datapath):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(datapath) as csv_file:
        csv_read = csv.DictReader(csv_file)

        for x in csv_read:
            coffee_in_ml.append(float(x['Coffee in ml']))
            sleep_in_hours.append(float(x['sleep in hours']))

        return {"x": coffee_in_ml,"y" :sleep_in_hours}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print(correlation[0,1])

def setup():
    datapath = 'data.csv'
    datasource = getdatasource(datapath)
    findcorrelation(datasource)
    plotfigure(datapath)

setup()

