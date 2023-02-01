
from rest_framework import serializers
from crudx.models import StudentsData


class ObjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentsData
    fields = '__all__' 


