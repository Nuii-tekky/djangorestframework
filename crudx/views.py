from django.shortcuts import render

# Create your views here.

def renderlanding(request):
  return render(request,'index.html')