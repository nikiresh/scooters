import typing as tp

from geopy.geocoders import Nominatim
from geopy.point import Point
from app import dto


class GeocoderClient:
    def __init__(self, user_agent) -> None:
        self.user_agent = user_agent
    
    def get_address(self, location: dto.Location) -> tp.Optional[str]:
        locator = Nominatim(user_agent=self.user_agent)
        return 'Some address'
        return locator.reverse(((location.lat, location.lon)))