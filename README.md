Basic Set Up:
* Create the virtual env
```python3 -m venv env```
* Activate the env
```source env/bin/activate```
* Install dependencies
```pip install -r requirements.txt```
* Run Server
```python3 manage.py runserver```
* Create a superuser
```python3 manage.py createsuperuser```
* Create Mock Server in Postman
* Create a Request in Mock Server using this endpoint
```v2/property/details```
* And this response
```
```
```
{
    "property/details": {
        "api_code_description": "ok",
        "api_code": 0,
        "result": {
            "property": {
                "air_conditioning": "yes",
                "attic": false,
                "basement": "full_basement",
                "building_area_sq_ft": 1824,
                "building_condition_score": 5,
                "building_quality_score": 3,
                "construction_type": "Wood",
                "exterior_walls": "wood_siding",
                "fireplace": false,
                "full_bath_count": 2,
                "garage_parking_of_cars": 1,
                "garage_type_parking": "underground_basement",
                "heating": "forced_air_unit",
                "heating_fuel_type": "gas",
                "no_of_buildings": 1,
                "no_of_stories": 2,
                "number_of_bedrooms": 4,
                "number_of_units": 1,
                "partial_bath_count": 1,
                "pool": true,
                "property_type": "Single Family Residential",
                "roof_cover": "Asphalt",
                "roof_type": "Wood truss",
                "site_area_acres": 0.119,
                "style": "colonial",
                "total_bath_count": 2.5,
                "total_number_of_rooms": 7,
                "sewer": "municipal",
                "subdivision" : "CITY LAND ASSOCIATION",
                "water": "municipal",
                "year_built": 1957,
                "zoning": "RH1"
            },

            "assessment":{
                "apn": "0000 -1111",
                "assessment_year": 2015,
                "tax_year": 2015,
                "total_assessed_value": 1300000.0,
                "tax_amount": 15199.86
            }
        }
    }
}
```
```
```
* Replace the 'HOUSE_CANARY_URL' in settings.py with your mock server url
```{mock server url}/v2/property/details```

* Finally create a request to the Django server, don't forget to provide basic authorization credentials of the user you created, ex:
```http://127.0.0.1:8000/api/v1/property_details/septic_system?address="park"&zipcode=03249```


Next steps:

* Set up unit tests for services, clients, and views
* Change authorization to something more advanced, OAuth, JWT
* Containerize this service for easy set up
* Investigate pros/cons between MySQL and PostGreSQL in this setting
* Seperate settings for dev, prod environments
* Store any secrets in AWS parameter store
* Cron job or AWS Lambda that syncs up the DB with HouseCanary API
* Add logging