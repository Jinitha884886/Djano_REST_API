from rest_framework.decorators import api_view
from rest_framework.response import Response

# www.  /api/index

@api_view(["GET"])
def index(request):
    people_details = {
        "name": "Jinitha",
        "age": 24,
        "job": "Junior software developer"
    }

    return Response(people_details)
