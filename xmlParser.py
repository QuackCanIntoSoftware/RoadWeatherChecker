from xml.etree import ElementTree as ET
import os
import sys


class xmlParser:
    def __init__(self):
        self.citiesList = [
            ["Bieruń", "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691"],
            ["Częstochowa", "/pl/pl/czstochowa/275785/hourly-weather-forecast/275785"]
        ]

    @staticmethod
    def __getWebpages(root):
        return [[page, page.find('NAME').text, page.find('WWW').text, page.find('CITIES')] for page in root.findall('PAGE')]

    @staticmethod
    def __getCityNamesAndLinks(page):
        return [[city, city.find('NAME').text, city.find('GETLINK').text] for city in page.findall('CITY')]

    @staticmethod
    def __getTimes(root):
        result = []
        for time in root.findall('TIME'):
            if time.find('TYPE').text == "hour":
                result.append([time.find('TYPE').text, time.find('HOUR').text, time.find('COUNT').text])
            elif time.find('TYPE').text == 'offset':
                result.append([time.find('TYPE').text, time.find('OFFSET').text, time.find('COUNT').text])
            else:
                pass
        return result
        # return [[time, time.find('TYPE').text, time.find('GETLINK').text] for time in root.findall('CITY')]

    @staticmethod
    def getConfiguration(filename):
        xmlTree = ET.parse(os.path.join(os.getcwd(), filename))
        root = xmlTree.getroot()
        if root:
            pages = xmlParser.__getWebpages(root)
            if not pages:
                print('kupa')

            citiesList = []
            for page in pages:
                for city in xmlParser.__getCityNamesAndLinks(page[3]):
                    citiesList.append([city[1], page[2], city[2]])



            print(xmlParser.__getTimes(root))

            # print(citiesList)

class xmlParserException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class xmlParserNoPagesLoadedError(xmlParserException):
    pass




        # pass

