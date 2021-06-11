import requests
from django.conf import settings
from rest_framework import serializers
import json


def get_property_details(street_address: str, zipcode: str) -> dict:
    '''
    Client method calls API for property details data, and returns the serialized data
    '''
    url = settings.HOUSE_CANARY_URL
    response = requests.get(url, params={'address': street_address, 'zipcode': zipcode})
    property_details = response.json()
    
    serializer = PropertyDetailSerializer(data=property_details['property/details'])
    serializer.is_valid(raise_exception=True)
    return serializer.data


# Nested serializers to serialize the nested json received from API
class PropertySerializer(serializers.Serializer):
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
    site_area_acres = serializers.FloatField()
    style = serializers.CharField(max_length=100)
    subdivision = serializers.CharField(max_length=100)
    total_bath_count = serializers.FloatField()
    total_number_of_rooms = serializers.IntegerField()
    water = serializers.CharField(max_length=100)
    year_built = serializers.IntegerField()
    zoning = serializers.CharField(max_length=100)


class AssessmentSerializer(serializers.Serializer):
    apn = serializers.CharField(max_length=100)
    assessment_year = serializers.IntegerField()
    tax_year = serializers.IntegerField()
    total_assessed_value = serializers.FloatField()
    tax_amount = serializers.FloatField()


class ResultSerializer(serializers.Serializer):
    property = PropertySerializer()
    assessment = AssessmentSerializer()


class PropertyDetailSerializer(serializers.Serializer):
    result = ResultSerializer()
    api_code_description = serializers.CharField(max_length=100)
    api_code = serializers.CharField(max_length=100)
