import lxml.html as xhtml
import socket

RECONNECTS = 10
class CitiesDescriptions:

    # def __init__(self, name, baseUrl, getLink, pageContent):
    #     self.name = name
    #     self.baseUrl = baseUrl
    #     self.currentGetLink = getLink
    #     if pageContent:
    #         self.currenteTree = xhtml.fromstring(pageContent)
    #     else:
    #         self.currenteTree = self.getWebPageeTree()
    #     self.valuesList = self.parseValuesFromCurrentWebPage()
    #
    #     self.nextEightHoursLink = ''

    def __init__(self, name, baseUrl, getLink):
        self.name = name
        self.baseUrl = baseUrl
        self.getLink = getLink
        self.currentGetLink = getLink
        self.currenteTree = None
        self.rawValuesList = []

        self.nextEightHoursLink = ''


    def getWebPageeTree(self):
        import http.client as ht
        reconnectCounter = 0


        if 0:
            while 1:
                try:
                    print(self.baseUrl+self.currentGetLink)
                    conn = ht.HTTPConnection(self.baseUrl, port=80, timeout=5)
                    conn.request("GET", self.currentGetLink)
                except TimeoutError:
                    reconnectCounter += 1
                    if reconnectCounter >= RECONNECTS:
                        raise TimeoutError
                except socket.timeout:
                    reconnectCounter += 1
                    if reconnectCounter >= RECONNECTS:
                        raise TimeoutError
                # except http.client.CannotSendRequest:
                #     print("kuupa")\
            print("Passed")
        else:
            conn = ht.HTTPConnection(self.baseUrl, port=80, timeout=5)
            conn.request("GET", self.currentGetLink)

        return xhtml.fromstring(conn.getresponse().read())
    
    def getWebPageContent(self, getLink):
        import http.client as ht
        conn = ht.HTTPConnection(self.baseUrl)
        conn.request("GET", getLink)
        return conn.getresponse().read()
        #print(wPageData)

    def parseValuesFromCurrentWebPage(self):

        overviewTable = []

        overviewTable.append([hour.xpath('div[1]/text()')[0] for hour in
                              self.currenteTree.xpath('//div[@class="hourly-table overview-hourly"]/table/thead/tr')[0].findall(
                                  'td')])  # Overview table: Hour
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table overview-hourly"]/table/tbody/tr[1]')[0].findall(
                                  'td')])  # Overview table: Temperature
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table overview-hourly"]/table/tbody/tr[2]')[0].findall(
                                  'td')])  # Overview table: Real Feel Temperature
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table overview-hourly"]/table/tbody/tr[3]')[0].findall(
                                  'td')])  # Overview table: Wind
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table precip-hourly"]/table/tbody/tr[1]')[0].findall(
                                  'td')])  # Rain table: Rain
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table precip-hourly"]/table/tbody/tr[2]')[0].findall(
                                  'td')])  # Rain table: Snow
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table precip-hourly"]/table/tbody/tr[3]')[0].findall(
                                  'td')])  # Rain table: Ice
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table sky-hourly"]/table/tbody/tr[2]')[0].findall(
                                  'td')])  # Sky table: Cloudy
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table sky-hourly"]/table/tbody/tr[3]')[0].findall(
                                  'td')])  # Sky table: Humidity
        overviewTable.append([val.xpath('span/text()')[0] for val in
                              self.currenteTree.xpath('//div[@class="hourly-table sky-hourly"]/table/tbody/tr[4]')[0].findall(
                                  'td')])  # Sky table: Dew point
        return overviewTable

    def getAdditionalParametersFromWebPage(self):
        # find link to web page with next 8 hours
        nextLink = self.currenteTree.xpath('//div[@class="control-bar hourly-control"]//a[@class="right-float"]')[0].get('href')
        self.nextEightHoursLink = nextLink[nextLink.find(self.baseUrl) + len(self.baseUrl):]

        self.pageCityName = self.currenteTree.xpath('// li[ @ id = "current-city-tab"] / a / span[@class="current-city"]/h1/text()')[0]

        self.pageDay = self.currenteTree.xpath('//div[@class="hourly-table overview-hourly"]/table/thead/tr/th/text()')[0].strip()
        print(self.pageDay)


    def addEightHours(self):
        if not self.nextEightHoursLink:
            self.getAdditionalParametersFromWebPage()

        if 1:
            self.currentGetLink = self.nextEightHoursLink
            self.currenteTree = self.getWebPageeTree()
            self.nextEightHoursLink = ''
            newValues = self.parseValuesFromCurrentWebPage()
        else:
            newValues = [['05', '06', '07', '08', '09', '10', '11', '12'], ['7°', '7°', '6°', '6°', '6°', '6°', '6°', '7°'], ['1°', '-1°', '1°', '0°', '-2°', '0°', '0°', '1°'], ['24 WSW', '24 SW', '24 SW', '28 WSW', '32 WSW', '32 WSW', '32 WSW', '32 WSW'], ['47%', '51%', '40%', '37%', '40%', '37%', '34%', '34%'], ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'], ['0%', '0%', '0%', '0%', '0%', '0%', '0%', '0%'], ['95%', '95%', '76%', '76%', '76%', '76%', '76%', '76%'], ['54%', '54%', '53%', '51%', '51%', '49%', '47%', '44%'], ['-2°', '-2°', '-3°', '-3°', '-4°', '-4°', '-4°', '-5°']]

        # print(self.valuesList)
        # print()
        # print(newValues)
        self.mergeWithRawValuesTable(newValues)

    def mergeWithRawValuesTable(self, newValues):
        if not self.rawValuesList:
            self.rawValuesList = newValues
        else:
            for i, sublist in enumerate(newValues):
                self.rawValuesList[i] = self.rawValuesList[i] + newValues[i]


        #tree = xhtml.fromstring(wPageData)

    def downloadDataInRange(self, start, end):
        currentHour = start
        self.rawValuesList = []

        while currentHour < end:
            self.currentGetLink = self.getLink+"?hour="+str(currentHour)
            self.currenteTree = self.getWebPageeTree()
            newValues = self.parseValuesFromCurrentWebPage()

            self.mergeWithRawValuesTable(newValues)
            currentHour += 8

    def printRawValues(self):
        [print(row) for row in self.rawValuesList]


    def __getHourData(self, sHour, eHour):
        print("Start hour:", sHour, "end hour:", eHour)

    def __getHourOffsetData(self, hour, count):
        print("Start:", hour, "for next", count)

    def __getOffsetData(self, start, count):
        print("Offset:", start, "for next", count)

    def __getNowData(self, count):
        print("From now for next", count)

    def getRawInfo(self, timeRange):
        print(timeRange)
        if timeRange[0] == 'hour':
            self.__getHourData(timeRange[1], timeRange[2])
        elif timeRange[0] == 'offset':
            self.__getOffsetData(timeRange[1], timeRange[2])
        elif timeRange[0] == 'houroffset':
            self.__getHourOffsetData(timeRange[1], timeRange[2])
        elif timeRange[0] == 'now':
            self.__getNowData(timeRange[1])

        return self.rawValuesList

    def getTodayFullInfo(self):
        self.todayTable = [[]]

        if not self.nextEightHoursLink:
            self.getAdditionalParametersFromWebPage()

        hourAdvance = int(self.nextEightHoursLink[self.nextEightHoursLink.find("?hour=")+6:])
        if hourAdvance < 24:
            self.todayTable = self.parseValuesFromCurrentWebPage()
        else:
            tempTable = self.parseValuesFromCurrentWebPage()
            endIndex = tempTable[0].index('00')
            print(endIndex)



        # self.currentGetLink = self.nextEightHoursLink
        # self.currenteTree = self.getWebPageeTree()
        # self.nextEightHoursLink = ''
        # newValues = self.parseValuesFromCurrentWebPage()

    def getTomorrowFullInfo(self):
        hour = 24
        tomorrowValues = [[]]

        self.currentGetLink = self.defaultGetLink + "?hour=" + str(hour)
        self.currenteTree = self.getWebPageeTree()
        tomorrowValues = self.parseValuesFromCurrentWebPage()

        while hour < 48:
            self.currentGetLink = self.defaultGetLink+"?hour="+str(hour)
            self.currenteTree = self.getWebPageeTree()
            newValues = self.parseValuesFromCurrentWebPage()

            for i, sublist in enumerate(newValues):
                tomorrowValues[i] = tomorrowValues[i] + newValues[i]
            hour += 8

        for subList in tomorrowValues:
            print(subList)

    def __getHourLimits(self, start, end, nowHour):
        if start <= nowHour:
            if end <= nowHour:
                #jutro
                timeMin = start + 24
                if end > start:
                    timeMax = end + 24
                else:
                    timeMax = end + 48
            else:
                # dzisiaj z dokonczeniem
                timeMin = nowHour
                timeMax = end
        else:
            if end > start:
                # to dzisiaj ale pozniej
                timeMin = start
                timeMax = end
            else:
                # dzisiaj ale dokonczenie jutro
                timeMin = start
                timeMax = end + 24

        # if start <= nowHour:
        #     timeMin = nowHour
        # else:
        #     timeMin = start
        #
        # if start <= end:
        #     # dokonczenie dzis
        #     timeMax = end
        # else:
        #     # dokonczenie jutro
        #     timeMax = 24 + end

        return [timeMin, timeMax]

    def __getOffsetLimits(self, offset, count, nowHour):
        timeMin = nowHour + offset
        timeMax = timeMin + count
        return [timeMin, timeMax]

    def __getHourOffsetLimits(self, start, count, nowHour):
        # TODO: bledne liczenie
        if start < nowHour:
            timeMin = start + 24
        # if start <= nowHour:
        #     timeMin = nowHour
        else:
            timeMin = start
        timeMax = timeMin + count
        return [timeMin, timeMax]

        # if start < nowHour:
        #     #juz dzisiaj byl, wiec jedzieny od jutra
        #     timeMin = start + 24
        #


    def __getNowLimits(self, count, nowHour):
        return [nowHour, nowHour + count]


    def filterData(self, time):
        import datetime
        nowHour = datetime.datetime.now().hour

        if time[0] == 'hour':
            tempTimes = self.__getHourLimits(time[1], time[2], nowHour)
        elif time[0] == 'offset':
            tempTimes = self.__getOffsetLimits(time[1], time[2], nowHour)
        elif time[0] == 'houroffset':
            tempTimes = self.__getHourOffsetLimits(time[1], time[2], nowHour)
        elif time[0] == 'now':
            tempTimes = self.__getNowLimits(time[1], nowHour)

        index = tempTimes[0] % 24
        shift = int(tempTimes[0]/24)

        #TODO: Nie podoba mi sie filtrowanie. Zaleczone przez pobieranie od biezacej godziny mimo wszystko
        start = (self.rawValuesList[0].index(str(index).zfill(2)) + shift * 24) - nowHour
        end = start + (tempTimes[1] - tempTimes[0])

        return [l[start:end] for l in self.rawValuesList]


