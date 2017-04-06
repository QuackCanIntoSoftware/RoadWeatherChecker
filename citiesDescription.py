import lxml.html as xhtml
import socket

RECONNECTS = 10
class CitiesDescriptions:

    def __init__(self, name, baseUrl, getLink, pageContent):
        self.name = name
        self.baseUrl = baseUrl
        self.currentGetLink = getLink
        if pageContent:
            self.currenteTree = xhtml.fromstring(pageContent)
        else:
            self.currenteTree = self.getWebPageeTree()
        self.valuesList = self.parseValuesFromCurrentWebPage()

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
        self.mergeWithValuesTable(newValues)

    def mergeWithValuesTable(self, newValues):
        for i, sublist in enumerate(newValues):
            self.valuesList[i] = self.valuesList[i] + newValues[i]


        #tree = xhtml.fromstring(wPageData)

    def getRawInfo(self, timeRange):
        return self.valuesList

    def addToCharts(self, charts):
        pass

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


        # TODO: ogarnianie do godziny 24

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

    # TODO: get 24h. Przenieśc get tomoroow i today do innej fukcji, a te zeby tylko ustalały zakres get24h(start)





