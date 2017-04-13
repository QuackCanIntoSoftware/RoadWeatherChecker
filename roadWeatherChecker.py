from xmlParser import XmlParser
from printer import Printer
from citiesDescription import CitiesDescriptions
import testValues


class RoadWeatherChecker:

    def __init__(self, configFile):
        #reading config file
        self.config = XmlParser(configFile)
        self.citiesData = [CitiesDescriptions(city[0], city[1], city[2]) for city in self.config.citiesList]

        self.printer = Printer()
        # self.results [ [time, page, city results, city results, ... ]...]
        self.results = []
        # self.citiesList = citiesList
        self.timeLimits = None
    
    def __getHourData(self, start, end, nowHour):
        if start <= nowHour:
            timeMin = nowHour
        else:
            timeMin = start

        if nowHour <= end:
            # dokonczenie dzis
            timeMax = end
        else:
            # dokonczenie jutro
            timeMax = 24 + end

        return[timeMin, timeMax]

    def __getOffsetData(self, offset, count, nowHour):
        timeMin = nowHour + offset
        timeMax = timeMin + count
        return [timeMin, timeMax]

    def __getHourOffsetData(self, start, count, nowHour):
        if start <= nowHour:
            timeMin = nowHour
        else:
            timeMin = start
        timeMax = timeMin + count
        return [timeMin, timeMax]

    def __getNowData(self, count, nowHour):
        return [nowHour, nowHour + count]


    def __determineMaxTime(self):
        import datetime
        nowHour = datetime.datetime.now().hour


        # TODO: obliczanie maksymalnej odleglosci czasowe

        timeLim = [nowHour + 24, nowHour]
        for time in self.config.timesList:
            if time[0] == 'hour':
                tempTimes = self.__getHourData(time[1], time[2], nowHour)
            elif time[0] == 'offset':
                tempTimes = self.__getOffsetData(time[1], time[2], nowHour)
            elif time[0] == 'houroffset':
                tempTimes = self.__getHourOffsetData(time[1], time[2], nowHour)
            elif time[0] == 'now':
                tempTimes = self.__getNowData(time[1], nowHour)
                pass

            if tempTimes[0] < timeLim[0]:
                timeLim[0] = tempTimes[0]
            if tempTimes[1] > timeLim[1]:
                timeLim[1] = tempTimes[1]

        self.timeLimits = timeLim



    def getValues(self):

        #brzydko w huj...
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
        self.__determineMaxTime()

        self.getValues()
        for res in self.results:
            print(res[2].name, self.printer.transformData(res[2].valuesList))


