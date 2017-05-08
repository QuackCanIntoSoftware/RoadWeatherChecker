from xmlParser import XmlParser
from printer import Printer
from citiesDescription import CitiesDescriptions
import testValues


class RoadWeatherChecker:

    def __init__(self, configFile):
        #reading config file
        self.config = XmlParser(configFile)
        self.citiesData = [CitiesDescriptions(city[0], city[1], city[2]) for city in self.config.citiesList]

        self.printer = Printer(self.config)
        # self.results [ [time, page, city results, city results, ... ]...]
        self.results = []
        # self.citiesList = citiesList
        self.timeLimits = None
    
    def __getHourLimits(self, start, end, nowHour):
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

    def __getOffsetLimits(self, offset, count, nowHour):
        timeMin = nowHour + offset
        timeMax = timeMin + count
        return [timeMin, timeMax]

    def __getHourOffsetLimits(self, start, count, nowHour):
        # if start < nowHour:
        #     timeMin = start + 24
        if start <= nowHour:
            timeMin = nowHour
        else:
            timeMin = start
        timeMax = timeMin + count
        return [timeMin, timeMax]

    def __getNowLimits(self, count, nowHour):
        return [nowHour, nowHour + count]


    def __determineMaxTime(self):
        import datetime
        nowHour = datetime.datetime.now().hour

        timeLim = [nowHour + 24, nowHour]
        for time in self.config.timesList:
            if time[0] == 'hour':
                tempTimes = self.__getHourLimits(time[1], time[2], nowHour)
            elif time[0] == 'offset':
                tempTimes = self.__getOffsetLimits(time[1], time[2], nowHour)
            elif time[0] == 'houroffset':
                tempTimes = self.__getHourOffsetLimits(time[1], time[2], nowHour)
            elif time[0] == 'now':
                tempTimes = self.__getNowLimits(time[1], nowHour)

            if tempTimes[0] < timeLim[0]:
                timeLim[0] = tempTimes[0]
            if tempTimes[1] > timeLim[1]:
                timeLim[1] = tempTimes[1]

        self.timeLimits = timeLim

    def __downloadData(self):
        for city in self.citiesData:
            city.downloadDataInRange(self.timeLimits[0], self.timeLimits[1])
            print(city.name+"=========================")
            city.printRawValues()
            print('\n\n\n')

    def __downloadDataDEBUG(self):
        for city in self.citiesData:
            if city.name == 'Bieruń':
                city.rawValuesList = [
                    ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00', '01',
                     '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09'],
                    ['9°', '10°', '11°', '12°', '12°', '13°', '13°', '12°', '12°', '11°', '11°', '10°', '9°', '9°', '8°', '7°', '7°', '6°', '5°', '5°', '4°', '5°', '5°', '6°', '6°', '7°', '8°', '8°', '9°', '9°', '8°', '8°', '7°', '6°', '5°', '4°', '3°', '2°', '2°', '2°', '1°', '0°', '1°', '1°', '1°', '2°', '3°', '5°'],
                    ['8°', '8°', '10°', '9°', '9°', '11°', '9°', '9°', '8°', '8°', '8°', '7°', '5°', '4°', '5°', '4°', '2°', '2°', '2°', '0°', '0°', '-1°', '0°', '-1°', '2°', '3°', '3°', '6°', '7°', '6°', '4°', '5°', '4°', '3°', '4°', '3°', '2°', '2°', '2°', '1°', '0°', '-1°', '0°', '0°', '0°', '1°', '2°', '1°'],
                    ['13 SSW', '15 SSW', '17 SSW', '18 SSW', '20 SW', '22 SW', '22 WSW', '22 WSW', '22 WSW', '18 WSW', '15 SW', '15 WSW', '15 W', '15 W', '15 W', '15 WNW', '17 WNW', '15 WNW', '15 WNW', '15 WNW', '17 WNW', '20 WNW', '22 WNW', '24 WNW', '26 WNW', '26 WNW', '26 WNW', '26 WNW', '26 WNW', '24 NW', '22 NW', '18 NW', '17 NW', '11 NNW', '9 NNW', '7 NNE', '7 ENE', '7 ESE', '7 SE', '7 SSE', '7 SSE', '7 SSE', '7 SSE', '7 SSE', '7 SE', '9 SE', '11 SE', '11 SE'],
                    ['49%', '57%', '49%', '57%', '58%', '49%', '58%', '40%', '34%', '37%', '43%', '47%', '51%', '51%', '47%', '47%', '51%', '47%', '47%', '51%', '47%', '44%', '47%', '51%', '47%', '47%', '51%', '47%', '44%', '47%', '51%', '47%', '48%', '52%', '15%', '11%', '11%', '11%', '11%', '7%', '0%', '0%', '0%', '0%', '0%', '2%', '48%', '52%'],
                    ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '1%', '1%', '1%', '1%', '1%', '2%', '4%', '4%', '4%', '4%', '4%', '2%', '0%', '0%'],
                    ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'],
                    ['97%', '93%', '90%', '90%', '90%', '90%', '90%', '90%', '87%', '78%', '69%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '63%', '47%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '25%', '32%', '39%', '47%', '41%', '36%', '31%', '33%', '35%', '37%', '55%', '73%', '95%', '95%'],
                    ['60%', '57%', '52%', '49%', '47%', '46%', '46%', '47%', '50%', '54%', '59%', '65%', '68%', '71%', '78%', '84%', '87%', '87%', '87%', '85%', '84%', '81%', '75%', '68%', '60%', '54%', '52%', '53%', '50%', '51%', '52%', '55%', '60%', '66%', '72%', '81%', '87%', '87%', '84%', '86%', '90%', '97%', '90%', '88%', '93%', '88%', '80%', '70%'],
                    ['2°', '2°', '2°', '1°', '1°', '2°', '1°', '1°', '2°', '2°', '3°', '3°', '4°', '4°', '4°', '5°', '5°', '4°', '3°', '2°', '2°', '1°', '1°', '0°', '-1°', '-2°', '-2°', '-1°', '-1°', '-1°', '-1°', '-1°', '0°', '0°', '1°', '1°', '1°', '0°', '0°', '0°', '-1°', '0°', '-1°', '-1°', '0°', '0°', '0°', '0°'],

                ]
            if city.name == 'Częstochowa':
                city.rawValuesList = [
                    ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09'],
                    ['10°', '11°', '11°', '12°', '12°', '13°', '13°', '13°', '13°', '11°', '10°', '9°', '9°', '9°', '8°', '6°', '6°', '5°', '4°', '4°', '3°', '4°', '4°', '5°', '6°', '6°', '7°', '7°', '7°', '8°', '7°', '7°', '6°', '5°', '4°', '3°', '2°', '2°', '2°', '1°', '1°', '1°', '1°', '0°', '1°', '2°', '3°', '4°'],
                    ['10°', '10°', '11°', '11°', '11°', '10°', '9°', '10°', '9°', '7°', '7°', '5°', '4°', '2°', '3°', '0°', '1°', '-1°', '-1°', '-2°', '-3°', '-3°', '-2°', '-1°', '-2°', '1°', '3°', '2°', '4°', '5°', '3°', '4°', '3°', '1°', '3°', '2°', '2°', '1°', '2°', '0°', '-1°', '-1°', '-1°', '-2°', '-1°', '-1°', '-1°', '2°'],
                    ['11 SW', '13 SW', '17 SW', '18 SW', '22 SW', '24 SW', '26 WSW', '26 WSW', '24 WSW', '20 W', '18 W', '18 WNW', '20 WNW', '20 WNW', '20 WNW', '20 WNW', '20 W', '18 W', '18 W', '18 W', '20 W', '24 W', '28 W', '30 W', '30 W', '30 WNW', '30 WNW', '28 WNW', '26 WNW', '24 NW', '20 NW', '18 NW', '15 NNW', '11 NNW', '9 N', '7 NE', '7 ESE', '7 SE', '7 SE', '7 SSE', '9 SSE', '9 SSE', '9 SSE', '9 SSE', '11 SSE', '11 SSE', '13 SE', '13 SE'],
                    ['47%', '51%', '47%', '43%', '43%', '47%', '51%', '47%', '48%', '52%', '40%', '34%', '40%', '58%', '49%', '58%', '43%', '51%', '47%', '34%', '34%', '37%', '43%', '47%', '51%', '47%', '47%', '51%', '47%', '47%', '51%', '47%', '48%', '52%', '12%', '8%', '8%', '8%', '8%', '5%', '0%', '0%', '0%', '0%', '0%', '2%', '52%', '48%'],
                    ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '1%', '5%', '5%', '5%', '5%', '5%', '3%', '0%', '0%'],
                    ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'],
                    ['86%', '90%', '90%', '90%', '90%', '90%', '90%', '90%', '90%', '89%', '85%', '90%', '95%', '99%', '99%', '99%', '98%', '94%', '91%', '87%', '64%', '41%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '70%', '48%', '39%', '30%', '21%', '18%', '16%', '13%', '30%', '47%', '64%', '76%', '87%', '70%', '70%'],
                    ['58%', '55%', '54%', '51%', '48%', '45%', '43%', '43%', '46%', '52%', '58%', '66%', '72%', '74%', '80%', '85%', '88%', '89%', '90%', '88%', '94%', '89%', '81%', '74%', '72%', '69%', '72%', '74%', '71%', '64%', '62%', '60%', '64%', '71%', '78%', '87%', '91%', '88%', '84%', '83%', '82%', '79%', '76%', '75%', '76%', '76%', '73%', '68%'],
                    ['2°', '2°', '2°', '2°', '2°', '1°', '1°', '1°', '1°', '2°', '3°', '3°', '4°', '4°', '4°', '4°', '4°', '3°', '3°', '2°', '2°', '2°', '2°', '1°', '1°', '1°', '2°', '3°', '2°', '2°', '0°', '0°', '0°', '1°', '1°', '1°', '1°', '0°', '-1°', '-1°', '-2°', '-2°', '-3°', '-4°', '-3°', '-2°', '-1°', '-1°'],
                    ]


    def __printAll(self):
        for time in self.config.timesList:
            for page in self.config.pagesList:
                self.printer.printOneWindow({city.name: city.filterData(time) for city in self.citiesData}, page, time)


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
        #self.__downloadData()
        self.__downloadDataDEBUG()
        #now data is downloaded
        # TODO: select what is needed using __get####Limits and print it.
        self.__printAll()

        # TODO: needs refactor. getValue is awfull.
        # self.getValues()
        # for res in self.results:
        #     print(res[2].name, self.printer.transformData(res[2].valuesList))


