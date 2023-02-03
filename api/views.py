from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import ObjectsSerializer
from crudx.models import StudentsData


@api_view(['GET'])
def first_api_response(request,format= None):
  db_objects= StudentsData.objects.all()
  serialized= ObjectsSerializer(db_objects,many= True)
  return Response(serialized.data)


# read,update and delete data by name8@api_view(['GET'])
def view_by_name(request,name,format= None):
  try:
    db_obj= StudentsData.objects.get(firstname= name)
  except StudentsData.DoesNotExist:
    return Response(status= status.HTTP_404_NOT_FOUND)

  serialized= ObjectsSerializer(db_obj,many= False)
  return Response(serialized.data)
  
