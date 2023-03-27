
from rest_framework import serializers
from crudx.models import StudentsData,RandomWord,images,testing,anothertesting
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= get_user_model()
    fields= '__all__'

class ObjectsSerializer(serializers.ModelSerializer): 
  class Meta:
    model = StudentsData
    fields = '__all__' 


class WordSerializer(serializers.ModelSerializer):
  class Meta:
    model = RandomWord
    fields = '__all__' 



class imageSerializer(serializers.ModelSerializer):
  class Meta:
    model= images
    fields= "__all__"


class testingSerializer(serializers.ModelSerializer):
  class Meta:
    model= testing
    fields= "__all__"



class anotherSerializer(serializers.ModelSerializer):
  class Meta:
    model= anothertesting
    fields="__all__"