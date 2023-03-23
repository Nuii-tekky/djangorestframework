from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializer import ObjectsSerializer,WordSerializer,imageSerializer,testingSerializer,anotherSerializer
from crudx.models import StudentsData,RandomWord,images,testing,anothertesting



# -----------------------------student data model cruding-----------------------

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



@api_view(['POST'])
def add_data(request,format= None):
  serializer= ObjectsSerializer(data= request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"saved": "user saved!!!!!!!!!!"})  
  else:
    return Response({"saved": "not saved"})  
  


@api_view(["PUT"])   
def update_data(request,id,format= None):
  try:
    db_obj= StudentsData.objects.get(id= id)
  except RandomWord.DoesNotExist:
    return Response({"error": "sorry we cant find this student!!!"}) 
  serialized= ObjectsSerializer(db_obj,data= request.data)  
  if serialized.is_valid():
    serialized.save()
    return Response({"details": "saved"})
  else:
    return Response({"details": "not updated!!!"}) 
  


#------------------------- randomword model cruding-----------------------------

@api_view(['GET'])
def view_word(request,id,format= None):
  try:
    db_obj= RandomWord.objects.get(id= id)
  except RandomWord.DoesNotExist:
    return Response({"details": "word not found"})

  serialized= WordSerializer(db_obj,many= False)
  return Response(serialized.data)


@api_view(['GET'])
def viewallwords(req):
  db_obj= RandomWord.objects.all()
  serialized= WordSerializer(db_obj,many= True)
  return Response({"details": serialized.data})


@api_view(['POST'])
def add_word(request,format= None):
  try:
    db_obj= RandomWord.objects.get(word= request.data['word'])
    print(db_obj)
    if db_obj != {} or db_obj is not None:
      return Response({"details": "sorry word is already there"})
  except RandomWord.DoesNotExist:
    serializer= WordSerializer(data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"details": "word saved"})
    else:
      return Response({"details": "failed to save word"})  


@api_view(["PUT"])   
def changeword(request,id,format= None):
  try:
    db_obj= RandomWord.objects.get(id= id)
  except RandomWord.DoesNotExist:
    return Response({"error": "sorry we cant find this object!!!!!!!!"}) 
  serialized= WordSerializer(db_obj,data= request.data)  
  if serialized.is_valid():
    serialized.save()
    return Response({"details": "saved"})
  else:
    return Response({"details": "not updated!!!"})  



# -------------------------image model cruding----------------------------------

@api_view(["GET"])
def get_image(request,title,format=None):
  try:
    db_obj= images.objects.get(title= title)
  except images.DoesNotExist:
    return Response({"details": "not found"})  
  serialized= imageSerializer(db_obj,many= False)  
  print(serialized.data)
  return Response({"details":serialized.data})


@api_view(["POST"])
def add_image(request):
  try:
    db_obj= images.objects.get(title= request.data['title'])
    print(db_obj)
    if db_obj != {} or db_obj is not None:
      return Response({"saved":"object exists"})
  except images.DoesNotExist:
    serializer= imageSerializer(data= request.data)
    header= request.headers["hello"]
    print(header)
    if serializer.is_valid():
      serializer.save()
      return Response({"saved": "image saved"})
    else:
      return Response({"saved": "image not saved"})  


@api_view(["GET"])
def getallimg(req):
  db_obj= images.objects.all()
  serialized= imageSerializer(db_obj,many= True)
  return Response({"details": serialized.data})



#---------------------------------random testing------------------------------- 

@api_view(["GET"])
def gettesting(req,namee):
  try:
    db_obj= testing.objects.get(name= namee)
  except testing.DoesNotExist:
    try:
      db_obj= testing.objects.get(nickname= namee)
    except testing.DoesNotExist:
      try:
        db_obj= testing.objects.get(email= namee)  
      except testing.DoesNotExist:
        res= Response({"details":"object not found"})
        return res
  serialized= testingSerializer(db_obj,many= False)      
  res= Response({"details":serialized.data})
  print(res["details"])
  return res


# ----------------------------------anotherrandom testing-----------------------
@api_view(["POST"])
def getanothertesting(req):
  try:
    db_obj= anothertesting.objects.get(title= req.data['title'],summary= req.data['summary'])
  except anothertesting.DoesNotExist:
    return Response({"details":"not found"})  
  serialised= anotherSerializer(db_obj,many=False)
  return Response({"details":serialised.data})

