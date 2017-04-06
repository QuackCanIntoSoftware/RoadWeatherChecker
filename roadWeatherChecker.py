from xmlParser import XmlParser
from printer import Printer
from citiesDescription import CitiesDescriptions
import testValues


class RoadWeatherChecker:

    def __init__(self, configFile):
        #reading config file
        self.config = XmlParser(configFile)
        self.printer = Printer()
        # self.results [ [time, page, city results, city results, ... ]...]
        self.results = []
        # self.citiesList = citiesList

    def getValues(self):

        for time in self.config.timesList:
            for page in self.config.pagesList:
                results = []
                for city in self.config.citiesList:
                    cityInfo = CitiesDescriptions(city[0], city[1], city[2])
                    cityInfo.getRawInfo(time)
                    self.results.append([time, page, cityInfo])
                    # results.append(currentCity.getRawInfo(time))
                    # print(results)

    def run(self):
        self.getValues()
        for res in self.results:
            print( res[2].name, self.printer.transformData(res[2].valuesList))


