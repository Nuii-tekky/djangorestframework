
from rest_framework import serializers
from crudx.models import StudentsData,RandomWord,images,testing


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