from core.services.property_details_service import property_details, has_septic_system
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_200_OK)
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


class PropertyDetailsView(GenericViewSet):
    '''
    Viewset for all views correlating with PropertyDetails, must be authenticated to hit this endpoint
    '''
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def septic_system(self, request):
        '''
        View for determining if given propertyDetail at address and zipcode has a septic system,
        and returns true or false. Address and zipcode parameters are required.
        '''
        address = request.query_params.get('address')
        zipcode = request.query_params.get('zipcode')
        if zipcode is None or address is None:
            return Response('Required Params not received', status=HTTP_400_BAD_REQUEST)
        septic_system = has_septic_system(address, zipcode)
        return Response({"has_septic_system": septic_system}, status=HTTP_200_OK)
