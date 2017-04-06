# from html import lxml
#import requests
#import http.client as ht
#from lxml import html, etree
from citiesDescription import CitiesDescriptions
from roadWeatherChecker import RoadWeatherChecker
import xmlParser
import testValues as tv


CONFIG_FILE = "config.xml"

pageUrl = "www.accuweather.com"
pageGetLink = "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691"



print("\n\n------------------------\n\n")

try:
    rwc = RoadWeatherChecker(CONFIG_FILE)

    rwc.run()

except FileNotFoundError:
    print("File", CONFIG_FILE, "doesn't exists or is not reachable")
except xmlParser.xmlParserNoPagesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)
except xmlParser.xmlParserNoCitiesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)
except xmlParser.xmlParserNoTimesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)


