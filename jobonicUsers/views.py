from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jobonicUsers.models import User
from jobonicUsers.serializers import UserSerializer

from blocks import auth, moments

@csrf_exempt
def user_list(request):
    """
    List all users
    """

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['salt'] = auth.generate_str(32)
        data['password'] = auth.hash_password(data['password'], data['salt'])
        data['created'] = moments.now()
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
           
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)


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
def user_login(request, user_name, password):
    try:
        user = User.objects.get(user_name=user_name)
    except User.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'POST':
        stored_pass = User.password
        stored_salt = User.salt

        if unhash_password(stored_salt, password, stored_pass):
            return JsonResponse({"status" : "success"}, status=200)
        