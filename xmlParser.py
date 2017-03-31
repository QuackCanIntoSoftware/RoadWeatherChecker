from xml.etree import ElementTree as ET
import os


class xmlParser:
    def __init__(self, configFilename):
        self.configFilename = configFilename
        self.citiesList = []
        self.timesList = []
        self.pagesList = []
        self.__getConfiguration()

    def reloadConfiguration(self):
        self.__init__(self.configFilename)

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

    def __getConfiguration(self):

        xmlTree = ET.parse(os.path.join(os.getcwd(), self.configFilename))
        root = xmlTree.getroot()
        if root:
            self.pagesList = xmlParser.__getWebpages(root)
            if not self.pagesList:
                raise xmlParserNoPagesLoadedError("pages = xmlParser.__getWebpages(root)", "No available webpages in "+self.configFilename)

            self.citiesList = []
            for page in self.pagesList:
                for city in xmlParser.__getCityNamesAndLinks(page[3]):
                    self.citiesList.append([city[1], page[2], city[2]])

            if not self.citiesList:
                raise xmlParserNoCitiesLoadedError("citiesList.append([city[1], page[2], city[2]])", "No available cities in "+self.configFilename)

            self.timesList = xmlParser.__getTimes(root)
            if not self.timesList:
                raise xmlParserNoTimesLoadedError("times = xmlParser.__getTimes(root)", "No available times ranges in "+self.configFilename)


class xmlParserException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class xmlParserNoPagesLoadedError(xmlParserException):
    pass


class xmlParserNoCitiesLoadedError(xmlParserException):
    pass

class xmlParserNoTimesLoadedError(xmlParserException):
    pass