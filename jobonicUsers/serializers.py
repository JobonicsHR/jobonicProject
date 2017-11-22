from rest_framework import serializers
from jobonicUsers.models import User, UserProfile, LoginSession


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email_address', 'user_name', 'salt', 'password', 'created', 'active', 'organisation')

class LoginSessionSerializer (serializers.ModelSerializer):
    class Meta:
        model = LoginSession
        fields = ('id', 'user_id', 'session_key', 'created', 'expire')

class UserProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'phone', 'email', 'address', 'marital_status', 'dob', 'nationality', 'personal_statement', 'website', 'skills', 'hobbies' )