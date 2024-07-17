from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer
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