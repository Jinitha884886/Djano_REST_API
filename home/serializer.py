from rest_framework import serializers
from home.models import Person, Team

from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):    #this class created for only showing "team_name" fields insted of all filed in the model "Team", table(Suppos more fields presented)
    class Meta:
        model = Team
        fields = ['team_name']

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only = True)
    team_info = serializers.SerializerMethodField()     # This for creating "tram_info" new field using serializer (not in the model)

    class Meta:
        model= Person
        fields= '__all__'
        depth = 1

    def get_team_info(self,obj):                         # "get_" key word and prefix "team_info"
        return "extra fields using serializer"
    
# ////////////////////////////////////////////////////////////////////

# Authentication
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Username Alrady Exists")
        
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError("EmailID Already Exists")
            
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()