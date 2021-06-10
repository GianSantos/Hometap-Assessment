import requests
from django.conf import settings
from rest_framework import serializers


def get_property_details(street_address: str, zipcode: str):
    url = settings.HOUSE_CANARY_URL
    response = requests.get(url, params={'address': street_address, 'zipcode': zipcode})
    serializer = PropertyDetailSerializer(data=response.json())
    serializer.is_valid(raise_exception=True)
    return serializer.data


class PropertyDetailSerializer(serializers.Serializer):
    air_conditioning = serializers.CharField(max_length=100)
    attic = serializers.BooleanField()
    basement = serializers.CharField(max_length=100)
    building_area_sq_ft = serializers.IntegerField()
    building_condition_score = serializers.IntegerField()
    building_quality_score = serializers.IntegerField()
    construction_type = serializers.CharField(max_length=100)
    exterior_walls = serializers.CharField(max_length=100)
    fireplace = serializers.BooleanField()
    full_bath_count = serializers.IntegerField()
    garage_parking_of_cars = serializers.IntegerField()
    garage_type_parking = serializers.CharField(max_length=100)
    heating = serializers.CharField(max_length=100)
    heating_fuel_type = serializers.CharField(max_length=100)
    no_of_buildings = serializers.IntegerField()
    no_of_stories = serializers.IntegerField()
    number_of_bedrooms = serializers.IntegerField()
    number_of_units = serializers.IntegerField()
    partial_bath_count = serializers.IntegerField()
    pool = serializers.BooleanField()
    property_type = serializers.CharField(max_length=100)
    roof_cover = serializers.CharField(max_length=100)
    roof_type = serializers.CharField(max_length=100)
    sewer = serializers.CharField(max_length=100)
    site_area_acres = serializers.IntegerField()
    style = serializers.CharField(max_length=100)
    subdivision = serializers.CharField(max_length=100)
    total_bath_count = serializers.IntegerField()
    total_number_of_rooms = serializers.IntegerField()
    water = serializers.CharField(max_length=100)
    year_built = serializers.IntegerField()
    zoning = serializers.CharField(max_length=100)
