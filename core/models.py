from django.db import models

# Create your models here.

class PropertyDetail(models.Model):
    # model to save/query property details instead of requesting from API all the time
    class Meta:
        # One property per address and zipcode
        unique_together = ['street_address', 'zipcode']

    street_address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    air_conditioning = models.CharField(max_length=100, null=True)
    attic = models.BooleanField(null=True)
    basement = models.CharField(max_length=100, null=True)
    building_area_sq_ft = models.IntegerField(null=True)
    building_condition_score = models.IntegerField(null=True)
    building_quality_score = models.IntegerField(null=True)
    construction_type = models.CharField(max_length=100, null=True)
    exterior_walls = models.CharField(max_length=100, null=True)
    fireplace = models.BooleanField(null=True)
    full_bath_count = models.IntegerField(null=True)
    garage_parking_of_cars = models.IntegerField(null=True)
    garage_type_parking = models.CharField(max_length=100, null=True)
    heating = models.CharField(max_length=100, null=True)
    heating_fuel_type = models.CharField(max_length=100, null=True)
    no_of_buildings = models.IntegerField(null=True)
    no_of_stories = models.IntegerField(null=True)
    number_of_bedrooms = models.IntegerField(null=True)
    number_of_units = models.IntegerField(null=True)
    partial_bath_count = models.IntegerField(null=True)
    pool = models.BooleanField(null=True)
    property_type = models.CharField(max_length=100, null=True)
    roof_cover = models.CharField(max_length=100, null=True)
    roof_type = models.CharField(max_length=100, null=True)
    sewer = models.CharField(max_length=100, null=True)
    site_area_acres = models.IntegerField(null=True)
    style = models.CharField(max_length=100, null=True)
    subdivision = models.CharField(max_length=100, null=True)
    total_bath_count = models.IntegerField(null=True)
    total_number_of_rooms = models.IntegerField(null=True)
    water = models.CharField(max_length=100, null=True)
    year_built = models.IntegerField(null=True)
    zoning = models.CharField(max_length=100, null=True)


    @classmethod
    def from_data(cls, data):
        '''
        Mapping data received to an instance without saving.
        '''
        instance = cls(street_address=data['street_address'], zipcode=data['zipcode'])
        data = data['result']['property']
        instance.air_conditioning = data['air_conditioning']
        instance.attic = data['attic']
        instance.basement = data['basement']
        instance.building_area_sq_ft = data['building_area_sq_ft']
        instance.building_condition_score = data['building_condition_score']
        instance.building_quality_score = data['building_quality_score']
        instance.construction_type = data['construction_type']
        instance.exterior_walls = data['exterior_walls']
        instance.fireplace = data['fireplace']
        instance.full_bath_count = data['full_bath_count']
        instance.garage_parking_of_cars = data['garage_parking_of_cars']
        instance.garage_type_parking = data['garage_type_parking']
        instance.heating = data['heating']
        instance.heating_fuel_type = data['heating_fuel_type']
        instance.no_of_buildings = data['no_of_buildings']
        instance.no_of_stories = data['no_of_stories']
        instance.number_of_bedrooms = data['number_of_bedrooms']
        instance.number_of_units = data['number_of_units']
        instance.partial_bath_count = data['partial_bath_count']
        instance.pool = data['pool']
        instance.property_type = data['property_type']
        instance.roof_cover = data['roof_cover']
        instance.roof_type = data['roof_type']
        instance.sewer = data['sewer']
        instance.site_area_acres = data['site_area_acres']
        instance.style = data['style']
        instance.subdivision = data['subdivision']
        instance.total_bath_count = data['total_bath_count']
        instance.total_number_of_rooms = data['total_number_of_rooms']
        instance.water = data['water']
        instance.year_built = data['year_built']
        instance.zoning = data['zoning']
        return instance
        
