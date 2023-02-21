from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializer import ObjectsSerializer
from crudx.models import StudentsData


@api_view(['GET'])
def first_api_response(request,format= None):
  db_objects= StudentsData.objects.all()
  serialized= ObjectsSerializer(db_objects,many= True)
  return Response(serialized.data)


# read,update and delete data by name8@api_view(['GET'])
@api_view(['GET'])
def view_by_name(request,name,format= None):
  try:
    db_obj= StudentsData.objects.get(firstname= name)
  except StudentsData.DoesNotExist:
    return Response(status= status.HTTP_404_NOT_FOUND)

  serialized= ObjectsSerializer(db_obj,many= False)
  return Response(serialized.data)



@api_view(['POST','PUT'])
def add_data(request,format= None):
  serializer= ObjectsSerializer(data= request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"saved": "user saved!!!!!!!!!!"})  
  else:
    return Response({"saved": "not saved"})  
  

# @api_view(['GET','PUT','DELETE'])
# def view_by_id(request,id,format= None):
#   try:
#     db_obj= StudentsData.objects.get(id= id)
#   except StudentsData.DoesNotExist:
#     return Response(status= status.HTTP_404_NOT_FOUND)  
#   if request.method== 'GET':
#     serialized= ObjectsSerializer(db_obj,many= False)
#     return Response(serialized.data)
#   elif request.method== 'PUT':
#     serialized = ObjectsSerializer(db_obj,data= request.data)
#     if serialized.is_valid():
#       serialized.save()
#       return Response(serialized.data)
#     else:
#       return Response(status= status.HTTP_400_BAD_REQUEST) 
  
