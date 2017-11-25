from rest_framework import serializers
from jobonicUsers.models import User, UserProfile, LoginSession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'first_name', 'middle_name', 'last_name', 'email_address', 'user_name', 'salt', 'password', 'date_created',
        'active', 'update_history')


class LoginSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginSession
        fields = ('id', 'user_id', 'session_key', 'created', 'expire', 'update_history')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
        'id', 'user_id', 'phone', 'social_facebook', 'social_twitter', 'social_linkedin', 'social_instagram', 'website',
        'address', 'marital_status', 'date_of_birth', 'gender', 'languages', 'nationality', 'personal_statement', 'date_created', 'update_history')
