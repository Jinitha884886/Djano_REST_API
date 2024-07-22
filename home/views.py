from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer, LoginSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

# Function based View
# www.  /api/index
@api_view(["GET", "POST", "PUT"])
def index(request):
    if request.method == "GET":
        people_details = {
            "name": "Jinitha",
            "age": 24,
            "job": "Junior software developer"
        }

        return Response(people_details)
    elif request.method == "POST":
        print("This is POST method")
        return Response("POST")
    
    elif request.method == "PUT":
        print("This is PUT method")
        return Response("PUT")


# People.objjects.all() =>  [1,2,3,4,5,............]  (queryset) => JSON => Serializers
 # /api/person

@api_view(["GET", "POST", "PUT", "PATCH","DELETE"])
def person(request):
    if request.method == "GET":
        objPerson = Person.objects.all()
        serializer = PersonSerializer(objPerson, many= True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        data = request.datas
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})

#/////////////////////////////////////////////////////////////////////
# class Based view using "ApiView"

# api/classperson/
class Classperson(APIView):
    def get(self, request):
        return Response("This is get method from APIView")
    def post(self, request):
        return Response("This is post method from APIView")

# api/personclassview/
class  PersonClassView(APIView):
    permission_classes = [IsAuthenticated]                           # "permission_classes" is inbuilt variable name
    authentication_classes = [TokenAuthentication]                   #  "authentication_classes" is inbuilt variable name
    def get (self, request):
        objPerson = Person.objects.all()
        serializer = PersonSerializer(objPerson, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})

#///////////////////////////////////////////////////////////////////////

# "View Set" is used to perform CRUD operations on Models

class PersonViewSets(viewsets.ModelViewSet):
    serializer_class = PersonSerializer         # "serializer_class" is permanent variable name
    queryset = Person.objects.all()

# ///////////////////////////////////////////////////////////////////////////

# queryparam(For searching)                                         URL/api/person/?search=ath
    def list(self, request):
        search = request.GET.get("search")
        queryset = self.queryset

        if search:
            queryset =queryset.filter(name__startswith = search)    #start with

        serializer = PersonSerializer(queryset, many =True)
        return Response({"status":200, "data": serializer.data})
    
    #////////////////////////////////////////////////////////////////////////////////////////////////

    #  Token Authentication

class RegisterAPI(APIView):
        def post(self, request):
            _data = request.data
            serializer = RegisterSerializer(data = _data)

            if not serializer.is_valid():
                return Response({'message': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
            
            serializer.save()

            return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        
class LoginAPI(APIView):
        permission_classes = [AllowAny]  
        def post(self, request):
            _data = request.data
            serializer = LoginSerializer(data = _data)

            if not serializer.is_valid():
                return Response({"message": serializer.errors}, status=status.HTTP_404_NOT_FOUND)

            user =authenticate(username= serializer.data['username'], password=serializer.data['password'])

            if not user:
                return Response({'message': "Invalid"}, status=status.HTTP_404_NOT_FOUND)
            token, _ =Token.objects.get_or_create(user=user)
            return Response({"message": "Login Successfilly", "token": str(token)}, status=status.HTTP_200_OK)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Permissions
