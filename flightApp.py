import urllib

import pymongo
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://Aidan:" + urllib.parse.quote_plus("W@sab1dog") + "@cluster0.uobls.mongodb.net/Flightdb?retryWrites=true&w=majority")
db = client.Flightdb
flights = db.Flights

app = Flask(__name__)


@app.route('/success/<flight>', )
def success(flight):
    return 'flight %s' % flight


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        flightReq = request.form
        flightDoc = flights.find({"dparture.iata": flightReq['origin'], "arrival.iata": flightReq['destination'],
                                  "flight_date": flightReq["date"]})
        flightData = [flight for flight in flightDoc]
        df = format_dataframe(flightData)

        return render_template('zulu_response.html', tables=[df.to_html(classes="data")])
    else:
        return render_template('zulu.html')


def format_dataframe(query):
    labels = ["ID", "Price", "Airline", "Departure IATA", "Departure Airport", "Departure Gate", "Departure Time", "Arrival IATA",
              "Arrival Airport", "Arrival Gate", "Arrival Time"]
    rows = []
    for flight in query:
        data = [flight["flight"]["number"], flight["flight"]["price"], flight["airline"]["name"], flight["dparture"]["iata"],
                flight["dparture"]["airport"], flight["dparture"]["gate"], flight["dparture"]["scheduled"],
                flight["arrival"]["iata"], flight["arrival"]["airport"], flight["arrival"]["gate"],
                flight["arrival"]["scheduled"]]
        rows.append(data)

    df = pd.DataFrame(rows, columns=labels)
    return df


if __name__ == '__main__':
    app.run(debug=True)
