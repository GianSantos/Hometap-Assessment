from core.services.property_details_service import property_details, has_septic_system
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import serializers


class PropertyDetailsView(GenericViewSet):
    def list(self, request):
        address = request.GET.get('address', None)
        zipcode = request.GET.get('zipcode', None)
        serializer = PropertyDetailSerializer(data={'address': address, 'zipcode': zipcode})
        serializer.is_valid(raise_exception=True)
        septic_system = has_septic_system(address, zipcode)
        return Response(septic_system)


# create serializer to validate params
class LocationSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=100)
    zipcode = serializers.CharField(max_length=100)