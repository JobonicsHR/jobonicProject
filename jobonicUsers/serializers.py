from rest_framework import serializers
from jobonicUsers.models import User


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'user_name', 'salt', 'password', 'created')