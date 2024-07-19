from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer
from rest_framework.views import APIView


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
# class Based view using ApiView

# api/classperson/
class Classperson(APIView):
    def get(self, request):
        return Response("This is get method from APIView")
    def post(self, request):
        return Response("This is post method from APIView")

# api/personclassview/
class  PersonClassView(APIView):
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


