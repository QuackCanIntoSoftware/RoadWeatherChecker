# from html import lxml
#import requests
#import http.client as ht
#from lxml import html, etree
from citiesDescription import CitiesDescriptions
import xmlParser


CONFIG_FILE = "config.xml"

pageUrl = "www.accuweather.com"
pageGetLink = "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691"

def cropNumbers(data):
    print(data)
    for i, value in enumerate(data[0]):
        print(i)




def showResults(data):
    import matplotlib.pyplot as plt

    data = cropNumbers(data)

    plt.plot([1,2,3,4])
    plt.show()

    print(data)
    pass

# conn = ht.HTTPConnection("www.accuweather.com")
# conn.request("GET", "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691")
# r1 = conn.getresponse()
# broken_html = r1.read()  # This will return entire content.

#
# print(broken_html)
# tree = html.fromstring(broken_html)
# print('Tree:',  tree.getchildren())
# print("\n--------------------------------------\n\n")


#nextLink = tree.xpath('//div[@class="control-bar hourly-control"]//a[@class="right-float"]')[0].get('href')
#nextLink = nextLink[nextLink.find(pageUrl)+len(pageUrl):]


print("\n\n------------------------\n\n")

try:
    config = xmlParser.xmlParser(CONFIG_FILE)

    if 1:
        for time in config.citiesList:
            for page in config.pagesList:
                results = []
                for city in config.citiesList:
                    # currentCity = CitiesDescriptions(city[0], pageUrl, pageGetLink, '')
                    # results.append(currentCity.getAllInfo(time))

                    #currentCity.addToCharts(charts)
                    pass
                results = [['05', '06', '07', '08', '09', '10', '11', '12'], ['7°', '7°', '6°', '6°', '6°', '6°', '6°', '7°'], ['1°', '-1°', '1°', '0°', '-2°', '0°', '0°', '1°'], ['24 WSW', '24 SW', '24 SW', '28 WSW', '32 WSW', '32 WSW', '32 WSW', '32 WSW'], ['47%', '51%', '40%', '37%', '40%', '37%', '34%', '34%'], ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'], ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'], ['95%', '95%', '76%', '76%', '76%', '76%', '76%', '76%'], ['54%', '54%', '53%', '51%', '51%', '49%', '47%', '44%'], ['-2°', '-2°', '-3°', '-3°', '-4°', '-4°', '-4°', '-5°']]

                showResults(results)




except FileNotFoundError:
    print("File", CONFIG_FILE, "doesn't exists or is not reachable")
except xmlParser.xmlParserNoPagesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)
except xmlParser.xmlParserNoCitiesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)
except xmlParser.xmlParserNoTimesLoadedError as e:
    print(e.message, "\nIn expression:", e.expression)



    #cd = CitiesDescriptions('Bierun', pageUrl, pageGetLink, broken_html)

    #cd = CitiesDescriptions('Bierun', broken_html)
    #cd.addEightHours()
    #cd.addEightHours()
    #for subList in cd.valuesList:
    #    print(subList)
