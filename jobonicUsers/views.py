from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from jobonicUsers.models import User, LoginSession
from jobonicUsers.serializers import UserSerializer, LoginSessionSerializer

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
        print (data)
        user_data = {
            "first_name" : data['firstName'],
            "last_name" : data['lastName'],
            "user_name" : data['id'],
            "linked_in_uid" : data['id'],
            "email_address" : data['emailAddress']
        }
        return JsonResponse(pack({}), status=200)
        # data['salt'] = auth.generate_str(32)
        # data['password'] = auth.hash_password(data['salt'], data['password'])
        # serializer = UserSerializer(data=data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(pack(serializer.data, True, "User Updated Successfully"), status=201)
        # return JsonResponse(pack (serializer.errors, False, "Error in data receieved"), status=400)


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
            return HttpResponse(status=400)

        stored_pass = user.password
        stored_salt = user.salt

        unhash = auth.unhash_password(stored_salt, data['password'], stored_pass)
        if unhash:
            new_session = LoginSession(user_id=user, created=moments.now(), expire=moments.now() + 3600)
            sess = LoginSessionSerializer(new_session)
            return JsonResponse(sess.data, safe=False)
        else:
            return JsonResponse({"msg": "Unsuccessfully"})
