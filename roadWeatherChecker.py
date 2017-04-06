from xmlParser import XmlParser
from printer import Printer
from citiesDescription import CitiesDescriptions
import testValues


class RoadWeatherChecker:

    def __init__(self, configFile):
        #reading config file
        self.config = XmlParser(configFile)
        self.printer = Printer()
        # self.citiesList = citiesList

    def getValues(self):

        for time in self.config.citiesList:
            for page in self.config.pagesList:
                results = []
                for city in self.config.citiesList:
                    currentCity = CitiesDescriptions(city[0], city[1], city[2], testValues.rawWebpage)
                    results.append(currentCity.getRawInfo(time))
                    # print(results)

    def run(self):
        self.getValues()
        self.printer.transformData(testValues.rawData)


