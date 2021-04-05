import requests
from bs4 import BeautifulSoup


def expedia_scrape(origin, destination, depart_date):
    url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:{},to:{},departure:{}TANYT&passengers=" \
          "adults:1,infantinlap:Y&mode=search".format(origin, destination, depart_date)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    labels = soup.findAll('label')
    ids = []
    for label in labels:
        if 'id' in label.attrs:
            ids.append(label)
    return ids
#wtf are you talking about


