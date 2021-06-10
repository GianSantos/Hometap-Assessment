# call client
from core.clients.property_details_client import get_property_details

def property_details(street_address: str, zipcode: str):
    # TODO: instead of always hitting houseCanary api we can store propertyDetails in db and attempt to query them, if not request information from houseCanary
    # TODO: type hinting for every method
    # TODO: clean up views
    # TODO: mocking api
    # TODO: unit tests service/client/views
    # TODO: authorization/middleware 
    data = get_property_details(street_address, zipcode)
    return data

def has_septic_system(street_address: str, zipcode: str):
    data = property_details(street_address, zipcode)
    septic_system = data.get('sewer', None)
    return True if septic_system else False
