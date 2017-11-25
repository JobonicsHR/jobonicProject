from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from jobonicUsers.models import User, LoginSession, UserProfile
from jobonicUsers.serializers import UserSerializer, LoginSessionSerializer, UserProfileSerializer

from blocks import auth, moments
from blocks.formatter import pack


@csrf_exempt
def user_list(request):
    """
    List all users
    """

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(pack(serializer.data), safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['salt'] = auth.generate_str(32)
        data['password'] = auth.hash_password(data['salt'], data['password'])
        data['created'] = moments.now()
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def new_linkedin_user(request):
    if request.method == 'POST':
        # Linked In Code
        data = JSONParser().parse(request)
        user_data = {
            "first_name": data['firstName'],
            "last_name": data['lastName'],
            "user_name": data['id'],
            "linked_in_uid": data['id'],
            "email_address": data['emailAddress'],
            "password": data['id']
        }

        user_data['salt'] = auth.generate_str(32)
        user_data['password'] = auth.hash_password(user_data['salt'], user_data['password'])
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            # save the user profile basic info - country, headline, pictureurl, linked_in url
            user_profile = {
                'user_title': data['headline'],
                'social_linkedin': data['publicProfileUrl'],
                'profile_picture': data['pictureUrl'],
                'country': data['location']['name'],
                'user_id' : serializer.data['id']
            }
            new_user_serializer = UserProfileSerializer(data=user_profile)
            return JsonResponse(pack(serializer.data, True, "User Updated Successfully"), status=201)
        return JsonResponse(pack(serializer.errors, False, "Error in data receieved"), status=400)


@csrf_exempt
def user_details(request, pk):
    """
    Retrieve, Update and Delete
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(email_address=data['email_address'])
        except User.DoesNotExist:
            return JsonResponse(pack({}, False, "Invalid Credentials"), status=404)

        stored_pass = user.password
        stored_salt = user.salt

        unhash = auth.unhash_password(stored_salt, data['password'], stored_pass)
        if unhash:
            new_session = LoginSession(user_id=user, created=moments.now(), expire=moments.now() + 3600)
            sess = LoginSessionSerializer(new_session)
            data = sess.data
            data['user_type'] = user.user_type
            return JsonResponse(pack(data), safe=False)
        else:
            return JsonResponse({"msg": "Unsuccessfully"})
