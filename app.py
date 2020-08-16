from flask import Flask, escape, request, render_template
# import pandas as pd
# import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/time')
def time():
    todays_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("time.html", todays_date =todays_date ) # , time = todays_date

@app.route('/COVID', methods = ['GET', 'POST'])
def corona():
    todays_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        return render_template("covid.html")
    elif request.method == 'GET':
        return render_template("covid.html", todays_date = todays_date)

# country = 'Finland'
# def covidStatus(country):
#     pop_df = pd.read_csv('output.csv')
#     pop = pop_df[pop_df.countriesAndTerritories == country]
#     fig, ax = plt.subplots()
#     ax.plot(pop.month.sort_values(), pop.cases.sort_values())

#     ax.set(xlabel='Month (s)', ylabel='covid-19 cases',
#            title='Covid19 in Finland')
    

#     fig.savefig("static\images\test.png")
#     plt.show()
    
    covidStatus(country)

if __name__ == "__main__":
    app.run(host='0.0.0.0')