import requests
from bs4 import BeautifulSoup
from selenium import webdriver


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


driver = webdriver.Chrome('C:/Users/sullivana6/PycharmProjects/Zulu/chromedriver')
driver.get('https://www.orbitz.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3ANew+York+%28NYC+-+All+Airports%29%2Cto%3AMiami+%28MIA+-+All+Airports%29%2Cdeparture%3A4%2F26%2F2021TANYT&options=cabinclass%3Aeconomy&leg2=from%3AMiami+%28MIA+-+All+Airports%29%2Cto%3ANew+York+%28NYC+-+All+Airports%29%2Cdeparture%3A4%2F27%2F2021TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate=4%2F26%2F2021&toDate=4%2F27%2F2021&d1=2021-04-26&d2=2021-04-27')
prices = driver.find_elements_by_xpath('//*[@id="flight-module-2021-04-26t06:30:00-04:00-coach-jfk-mia-aa-2268_2021-04-27t06:29:00-04:00-coach-mia-dca-aa-491-coach-dca-lga-aa-2117_"]/div[2]/div[2]/div[2]/div/div[1]/div[1]/span')[0]
print(prices)
print(type(prices))
