# Introduction
This is a recreation of an online travel agency for our software engineering class. We're working on an interface to search for flights and rank them by price, comfort, duration etc. The project ended up being good practice with end to end development. Currently we have a user interface where users can look up and book flights stored in our database. 

# Functions
1. Search for a flight
   * Search one way flight
   * Search round trip flight
2. Book a Flight
   * Checkout

# Installation
Start by cloning this repostory.

    > git clone git://github.com/rodriguezcorraless/Zulu

Make sure python3 is installed.  
The running environment requires Flask and Pandas. 
https://flask.palletsprojects.com/en/1.1.x/installation/
https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

We used the pymongo interface to interact to preform database operations.


#Run
From your IDE or commandline run the server file flight_app.py.

    $python flight_app.py

Next open the main html template zulu.html in your web browser. You should be able to search for flights based on location and date.
