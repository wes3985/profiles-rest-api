from django.shortcuts import render
from rest_framework.views import APIView    # 26
from rest_framework.response import Response # 26

# Create your views here.
class HelloApiView(APIView):
    """Test API View functionality"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as funtion (get, post, pathc, put, delete)',
            'similar to traditional django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        # The return object is a dictionary which has been converted to json
        # this will be rendered to the html webpage
        return Response({'message':'Hello!','an_apiview':an_apiview})
