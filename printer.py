from xmlParser import XmlParser

import matplotlib.pyplot as plt

class Printer:

    def __init__(self, config):
        self.config = config

    def __removeNonDigits(self, iList):
        oList = []
        for s in iList:
            oList.append(int(''.join([i for i in s if i.isdigit()])))
        return oList

    def transformData(self, iData):
        return [self.__removeNonDigits(row) for row in iData]

    def printOneWindow(self, dataDict, page, time):
        print("print one:\n", dataDict)

        print(len(list(dataDict.values())[0]))

        for key, value in dataDict.items():
            print(key)
            [print(val) for val in value]
        diction = {}

        #

        pass

    def showResults(data):

        data = cropNumbers(data)

        plt.plot([1, 2, 3, 4])
        plt.show()

        print(data)
        pass

