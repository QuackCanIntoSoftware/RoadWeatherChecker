import math

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

    def __determineFigureSize(self, nPlots):
        sqrt = math.sqrt(nPlots)
        sqrtRnd = int(sqrt)

        if sqrt - sqrtRnd == 0:
            return sqrtRnd, sqrtRnd
        elif sqrtRnd*sqrtRnd + sqrtRnd < nPlots:
            return sqrtRnd + 1, sqrtRnd + 1
        else:
            return sqrtRnd, sqrtRnd + 1

    def __addToSizeLegendRow(self, actualSize):
        return actualSize[0]+1, actualSize[1]

    def __prepareFigure(self, sizeTuple, name, data, selectedDataDict):
        i = 1
        #for title, index in selectedDataList.items():
        for title, index in sorted(selectedDataDict.items(), key=lambda x: x[1]):
            plt.subplot(*sizeTuple, i)
            plt.title(title)
            line, = plt.plot(range(0, len(data[index])), data[index], label=name)
            plt.xticks(range(0, len(data[0])), data[0])
            i += 1
        return line

    def __generateFigureTitle(self, page, time):
        if time[0] == 'houroffset':
            return "Hour offset from {:} for {:} hours".format(time[1], time[2])
        elif time[0] == 'hour':
            return "Hours from from {:} to {:}".format(time[1], time[2])
        elif time[0] == 'offset':
            return "Offset from now by {:} for {:} hours".format(time[1], time[2])
        elif time[0] == 'now':
            return "From now for next {:} hours".format(time[1])

    def __getVisibleDict(self):
        result = []
        for key, value in self.config.displayConfigDict.items():
             if value[0]:
                 result.append(int(value[1]['position']))
                 # print(value[1])
        result = {v[1]['text']: int(v[1]['position']) for k, v in self.config.displayConfigDict.items() if v[0]}
        # result.sort()
        return result
        pass



    def printOneWindow(self, dataDict, page, time):
        #plt.ion()
        plt.figure().suptitle(self.__generateFigureTitle(page, time))
        # TODO: plt.get_current_fig_manager().window.state('zoomed')
        visibleDict = self.__getVisibleDict()
        size = self.__addToSizeLegendRow(self.__determineFigureSize(len(visibleDict.keys())))

        legend = []
        for key, value in dataDict.items():
            #print(key)
            [print(val) for val in value]

            source = self.transformData(value)

            legend.append(self.__prepareFigure(size, key, source, visibleDict))

            plt.legend(handles=legend, bbox_to_anchor=(0.5, -0.75), loc=8, ncol=size[0]*2)

        #plt.title()
        plt.tight_layout()
        plt.show()


    # def showResults(data):
    #
    #     data = cropNumbers(data)
    #
    #     plt.plot([1, 2, 3, 4])
    #     plt.show()
    #
    #     print(data)
    #     pass

