import urllib
import datetime
import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://Aidan:" + urllib.parse.quote_plus("W@sab1dog") + "@cluster0.uobls.mongodb.net/Flightdb?retryWrites=true&w=majority")
db = client.Flightdb
flights = db.Flights
flightDoc = {"flight_date": "2021-03-17", "flight_status": "scheduled",
             "dparture":{"airport": "Adolfo Suárez Airport", "timezone": "Europe/Spain", "iata": "MAD", "icao": "KBOS",
                          "terminal": "T3", "gate": "H22", "delay": None, "scheduled": "2021-03-14T10:00:00+00:00",
                          "estimated": "2021-03-17T15:00:00+00:00", "actual": None, "estimated_runway": None,
                          "actual_runway": None},
             "arrival": {"airport": "Logan International Airport", "timezone": "Europe\/Amsterdam", "iata": "BOS", "icao": "EHAM",
                         "terminal": "B", "gate": "B10", "baggage": None, "delay": None,
                         "scheduled": "2021-03-17T12:07:00+00:00", "estimated": "2021-03-17T12:05:00+00:00",
                         "actual": None, "estimated_runway": None, "actual_runway": None},
             "airline": {"name": "United Airlines", "iata": "UA", "icao": "DAL"},
             "flight": {"number": "4153", "iata": "DL3097", "icao": "DAL3097", "price":"306",
                        "codeshared": {"airline_name": "uia", "airline_iata": "ps", "airline_icao": "aui",
                                       "flight_number": "101", "flight_iata": "ps101", "flight_icao": "aui101"}},
             "aircraft": None, "live": None}, \
            {"flight_date": "2021-03-17", "flight_status": "scheduled",
             "dparture":{"airport": "Adolfo Suárez Airport", "timezone": "America/New_York", "iata": "MAD", "icao": "KBOS",
                          "terminal": "T1", "gate": "H14", "delay": None, "scheduled": "2021-03-14T6:00:00+00:00",
                          "estimated": "2021-03-17T10:00:00+00:00", "actual": None, "estimated_runway": None,
                          "actual_runway": None},
             "arrival": {"airport": "Logan International Airport", "timezone": "Europe\/Amsterdam", "iata": "BOS", "icao": "EHAM",
                         "terminal": "E", "gate": "E7", "baggage": None, "delay": None,
                         "scheduled": "2021-03-17T12:14:00+00:00", "estimated": "2021-03-17T12:05:00+00:00",
                         "actual": None, "estimated_runway": None, "actual_runway": None},
             "airline": {"name": "Delta", "iata": "DL", "icao": "DAL"},
             "flight": {"number": "4179", "iata": "DL3097", "icao": "DAL3097", "price":"$479",
                        "codeshared": {"airline_name": "uia", "airline_iata": "ps", "airline_icao": "aui",
                                       "flight_number": "101", "flight_iata": "ps101", "flight_icao": "aui101"}},
             "aircraft": None, "live": None}
#flights.insert_many(flightDoc)





