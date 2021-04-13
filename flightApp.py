import urllib

import pymongo
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://Aidan:" + urllib.parse.quote_plus(
    "W@sab1dog") + "@cluster0.uobls.mongodb.net/Flightdb?retryWrites=true&w=majority")
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
        if not flightReq['r_date']:
            flightDoc = flights.find({"dparture.iata": flightReq['origin'], "arrival.iata": flightReq['destination'],
                                      "flight_date": flightReq["d_date"]})
            flightData = [flight for flight in flightDoc]
            df = format_oneway(flightData)
        else:
            flightDoc1 = flights.find({"dparture.iata": flightReq['origin'], "arrival.iata": flightReq['destination'],
                                      "flight_date": flightReq["d_date"]})
            flightDoc2 = flights.find({"dparture.iata": flightReq['destination'], "arrival.iata": flightReq['origin'],
                                      "flight_date": flightReq["r_date"]})
            zipped_query = zip(flightDoc1, flightDoc2)
            df = format_roundtrip(zipped_query)

        return render_template('zulu_response.html', tables=[flight.to_html(classes="data") for flight in df])
    else:
        return render_template('zulu.html')


def format_oneway(query):
    labels = ["ID", "Price", "Airline", "Departure IATA", "Departure Airport", "Departure Gate", "Departure Time",
              "Arrival IATA",
              "Arrival Airport", "Arrival Gate", "Arrival Time"]
    print(type(query))
    print(query)
    frames = []
    for flight in query:
        data = [flight["flight"]["number"], flight["flight"]["price"], flight["airline"]["name"],
                flight["dparture"]["iata"],
                flight["dparture"]["airport"], flight["dparture"]["gate"], flight["dparture"]["scheduled"],
                flight["arrival"]["iata"], flight["arrival"]["airport"], flight["arrival"]["gate"],
                flight["arrival"]["scheduled"]]
        res = dict(zip(labels, data))
        df = pd.DataFrame(res, index=[0])
        frames.append(df)

    return frames


def format_roundtrip(query):
    labels = ["ID", "Price", "Airline", "Departure IATA", "Departure Airport", "Departure Gate", "Departure Time",
              "Arrival IATA",
              "Arrival Airport", "Arrival Gate", "Arrival Time"]
    frames = []

    for flight1, flight2 in query:
        data = [[flight1["flight"]["number"], flight2["flight"]["number"]], [flight1["flight"]["price"], flight2["flight"]["price"]], [flight1["airline"]["name"], flight2["airline"]["name"]],
                [flight1["dparture"]["iata"], flight2["dparture"]["iata"]],
                [flight1["dparture"]["airport"], flight2["dparture"]["airport"]], [flight1["dparture"]["gate"], flight2["dparture"]["gate"]], [flight1["dparture"]["scheduled"], flight2["dparture"]["scheduled"]],
                [flight1["arrival"]["iata"], flight2["arrival"]["iata"]], [flight1["arrival"]["airport"], flight2["arrival"]["gate"]],
                [flight1["arrival"]["scheduled"], flight2["arrival"]["scheduled"]]]
        res = dict(zip(labels, data))
        df = pd.DataFrame(res, index=[0, 1])
        frames.append(df)

    return frames


if __name__ == '__main__':
    app.run(debug=True)
