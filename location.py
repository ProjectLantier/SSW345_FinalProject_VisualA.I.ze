class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude
    
    def get_latitude(self) -> float:
        return self.latitude
    
    def get_longitude(self) -> float:
        return self.longitude
