from django.shortcuts import render

# Create your views here.

def renderlanding(request):
  return render(request,'index.html')


def render_input(request):
  return render(request,'brandnew.html')

def render_testing(request):
  return render(request,"testing.html")

