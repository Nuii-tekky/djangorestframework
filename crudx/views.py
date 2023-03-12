from django.shortcuts import render,redirect
from django.http.response import HttpResponse

# Create your views here.

def renderlanding(request):
  return render(request,'index.html')


def render_input(request):
  return render(request,'addstudent.html')

def render_testing(request):
  return render(request,"getstudent.html")


def render_final_testing_1(request):
  return render(request,"addword.html")


def render_image_form(request):
  return render(request,"upload_img.html")

def render_get_image(request):
  return render(request,"getImage.html")

def render_checker(request):
  return render(request,"render.html")  

def render_dynamic(request):
  print(request.headers["details"])
  if request.headers["details"]== "render_desktop":
    return redirect("desktop")
  elif request.headers["details"]== "render_mobile":
    return redirect("mobile")
  else: 
   return  HttpResponse({"details":"please define your headers"})  
  

def render_desktop(request):
  return render(request,"desktop.html")


def render_mobile(request):
  return render(request,"mobile.html")

def render_multitry(req):
  return render(req,"multitry.html")
  

def render_all_words(req):
  return render(req,"allobj.html")





