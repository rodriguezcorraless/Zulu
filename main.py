import urllib

import pymongo

client = pymongo.MongoClient("mongodb+srv://Aidan:" + urllib.parse.quote_plus("W@sab1dog") + "@cluster0.uobls.mongodb.net/Flightdb?retryWrites=true&w=majority")
db = client.Flightdb
flights = db.Flights
#flightDoc = {"flight_date":"2021-03-14","flight_status":"scheduled","dparture":{"airport":"Boryspil (Borispol)","timezone":"Europe\/Kiev","iata":"KBP","icao":"UKBB","terminal":"D","gate":"D16","delay":None,"scheduled":"2021-03-14T10:00:00+00:00","estimated":"2021-03-14T10:00:00+00:00","actual":None,"estimated_runway":None,"actual_runway":None},"arrival":{"airport":"Schiphol","timezone":"Europe\/Amsterdam","iata":"AMS","icao":"EHAM","terminal":None,"gate":"G2","baggage":None,"delay":None,"scheduled":"2021-03-14T12:05:00+00:00","estimated":"2021-03-14T12:05:00+00:00","actual":None,"estimated_runway":None,"actual_runway":None},"airline":{"name":"KLM","iata":"KL","icao":"KLM"},"flight":{"number":"3097","iata":"KL3097","icao":"KLM3097","codeshared":{"airline_name":"uia","airline_iata":"ps","airline_icao":"aui","flight_number":"101","flight_iata":"ps101","flight_icao":"aui101"}},"aircraft":None,"live":None},{"flight_date":"2021-03-14","flight_status":"scheduled","departure":{"airport":"Boryspil (Borispol)","timezone":"Europe\/Kiev","iata":"KBP","icao":"UKBB","terminal":"D","gate":"D2","delay":None,"scheduled":"2021-03-14T09:50:00+00:00","estimated":"2021-03-14T09:50:00+00:00","actual":None,"estimated_runway":None,"actual_runway":None},"arrival":{"airport":"Ataturk Airport","timezone":"Europe\/Istanbul","iata":"IST","icao":"LTFM","terminal":None,"gate":None,"baggage":None,"delay":None,"scheduled":"2021-03-14T12:50:00+00:00","estimated":"2021-03-14T12:50:00+00:00","actual":None,"estimated_runway":None,"actual_runway":None},"airline":{"name":"Turkish Airlines","iata":"TK","icao":"THY"},"flight":{"number":"458","iata":"TK458","icao":"THY458","codeshared":None},"aircraft":None,"live":None}
#flights.insert_many(flightDoc)
location = input("Location")
doc = flights.find({"departure.airport":location})
for x in doc:
    print(x)
