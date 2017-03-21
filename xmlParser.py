from xml.etree import ElementTree as ET


class xmlParser:
    def __init__(self):
        self.citiesList = [
            ["Bieruń", "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691"],
            ["Częstochowa", "/pl/pl/czstochowa/275785/hourly-weather-forecast/275785"]
        ]

    @staticmethod
    def __getNamesAndLinks():
        pass

    @staticmethod
    def getConfiguration(filename):
        xmlTree = ET.parse(os.path.join(os.path.dirname(sys.argv[0]), filename))
        root = xmlTree.getroot()
        if root:

        xmlParser.__getNamesAndLinks()
        pass

