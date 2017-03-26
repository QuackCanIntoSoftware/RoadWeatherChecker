import lxml.html as xhtml

from xml.etree import ElementTree as ET

class xmlParser:
    def __init__(self):
        self.citiesList = [
            ["Bieruń", "/pl/pl/bieru/2659691/hourly-weather-forecast/2659691"],
            # ["Mysłowice", "/pl/pl/mysowice/265979/hourly-weather-forecast/265979"],
            # ["Dąbrowa Górnicza", "/pl/pl/dbrowa-gornicza/265977/hourly-weather-forecast/265977"],
            # ["Siewierz", "/pl/pl/siewierz/266017/hourly-weather-forecast/266017"],
            # ["Koziegłowy", "/pl/pl/koziegowy/1402295/hourly-weather-forecast/1402295"],
            # ["Wrzosowa", "/pl/pl/wrzosowa/275754/hourly-weather-forecast/275754"],
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

