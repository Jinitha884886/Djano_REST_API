from rest_framework import serializers
from home.models import Person, Team

class TeamSerializer(serializers.ModelSerializer):    #this class created for only showing "team_name" fields insted of all filed in the "Team" table(Suppos more fields presented)
    class Meta:
        model = Team
        fields = ['team_name']

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    team_info = serializers.SerializerMethodField()     # This for creating "tram_info" new field using serializer (not in the model)

    class Meta:
        model= Person
        fields= '__all__'
        depth = 1

    def get_team_info(self,obj):                         # "get_" key word and prefix "team_info"
        return "extra fields using serializer"