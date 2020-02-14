#create a class city with attributes lat, lon

class City:

    def __init__(self,name,lat,lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'({self.name}, {self.lat}, {self.lon})'