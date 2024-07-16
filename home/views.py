from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        return Response("POST")
    
    elif request.method == "PUT":
        return Response("PUT")
