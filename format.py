import requests
import random
import urllib
import pymongo

#File is designed to call the aviationstack flight api and format an insertion into the database

#establish connection to the flight database
client = pymongo.MongoClient("mongodb+srv://Aidan:" + urllib.parse.quote_plus(
    "") + "@cluster0.uobls.mongodb.net/Flightdb?retryWrites=true&w=majority")
db = client.Flightdb
flights = db.Flights


#calls flight api with parameters from main application file
#formats and inserts recieved flights into the flight database
def atlas_insert(origin, destination, date):
    params = {
        'access_key': '',
        'limit': 3,
        'dep_iata': origin,
        'arr_iata': destination,
        'flight_date': date
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()
    flight_doc = api_response['data']

    for flight in flight_doc:
        flight['flight']['price'] = '$' + str(random.randrange(50, 500))

    flights.insert_many(flight_doc)
    print(flight_doc)
    return flight_doc


params = {
    'access_key': '',
    'limit': 4,
    'dep_iata': 'BOS',
    'arr_iata': 'JFK',
}
api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
api_response = api_result.json()
