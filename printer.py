from xmlParser import XmlParser

class Printer:

    def __removeNonDigits(self, iList):
        oList = []
        for s in iList:
            oList.append(int(''.join([i for i in s if i.isdigit()])))
        return oList

    def transformData(self, iData):
        return [self.__removeNonDigits(row) for row in iData]


    def showResults(data):
        import matplotlib.pyplot as plt

        data = cropNumbers(data)

        plt.plot([1, 2, 3, 4])
        plt.show()

        print(data)
        pass

