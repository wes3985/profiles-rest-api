
#30
from rest_framework import serializers

from . import models  #41

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)  # checks that we've entered a char field with max len 10

#41
class UserProfileSerializer(serializers.ModelSerializer):
    """a serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
