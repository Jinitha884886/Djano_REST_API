from django.urls import path, include
from home.views import index, person, Classperson, PersonClassView, PersonViewSets, RegisterAPI, LoginAPI
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'person', PersonViewSets, basename="person")         # ModelViewSets default router code for urls
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name="index"),
    path('person/', person, name="person"),
    path('classperson/', Classperson.as_view(), name="classperson"),
    path('personclassview/', PersonClassView.as_view(), name= "personclassview"),
    path('register/', RegisterAPI.as_view(), name= "register"),
    path('login/', LoginAPI.as_view(), name= "login"),
    


]