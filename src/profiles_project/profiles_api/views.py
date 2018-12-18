from django.shortcuts import render
from rest_framework.views import APIView    # 26
from rest_framework.response import Response # 26
from rest_framework import status # 30

from . import serializers       # 30

# Create your views here.
class HelloApiView(APIView):
    """Test API View functionality"""

    # 30
    serializer_class =  serializers.HelloSerializer
    # 26
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

    # 30
    def post(self, request):
        """Creat a hello message with our name"""
        serializer =  serializers.HelloSerializer(data=request.data) # passes in the data from request
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)      # creates a string passing the name between the curly brackets
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)          # returns the errors log which is assinged to the serializer

    # 32
    def put(self, request, pk=None):
        """Handles updating an object"""
        #pk stands for primary key: the id for an object in the db
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method':'delete'})
