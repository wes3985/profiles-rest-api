from django.shortcuts import render
from rest_framework import viewsets            # 35
from rest_framework.views import APIView    # 26
from rest_framework.response import Response # 26
from rest_framework import status # 30
from rest_framework.authentication import TokenAuthentication # 46

from . import serializers       # 30
from . import models #42
from . import permissions # 46

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

# 35
class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    # 38
    serializer_class = serializers.HelloSerializer

    #35
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically map to URLS using Routers',
            'Provides more funtionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    #38
    def create(self, request):
        """Creat a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #38
    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method': 'GET'})

    #38
    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({'http_method': 'PUT'})

    #38
    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""
        return Response({'http_method': 'DELETE'})

#42
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #46
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
