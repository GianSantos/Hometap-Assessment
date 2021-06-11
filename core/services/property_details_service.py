# call client
from core.clients.property_details_client import get_property_details
from core.models import PropertyDetail


def property_details(street_address: str, zipcode: str) -> PropertyDetail:
    '''
    Service method that will perform the logic for the view, creating/querying propertydetail or calling client to request data from API,
    storing and querying PropertyDetails will help lessen calls to the third party API
    '''
    home = PropertyDetail.objects.filter(street_address=street_address, zipcode=zipcode).first()
    if home:
        return home
    data = get_property_details(street_address, zipcode)
    data['street_address'] = street_address
    data['zipcode'] = zipcode
    new_home = PropertyDetail.from_data(data)
    new_home.save()
    return new_home


def has_septic_system(street_address: str, zipcode: str) -> bool:
    '''
    Service method that calls on property_details to receive PropertyDetail and determine if property has a septic system
    '''
    data = property_details(street_address, zipcode)
    septic_system = data.sewer
    return True if septic_system else False
