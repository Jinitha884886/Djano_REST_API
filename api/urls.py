from django.urls import path
from home.views import index, person, Classperson, PersonClassView


urlpatterns = [
    path('index/', index, name="index"),
    path('person/', person, name="person"),
    path('classperson/', Classperson.as_view(), name="classperson"),
    path('personclassview/', PersonClassView.as_view(), name= "personclassview"),

]