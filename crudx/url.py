
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.renderlanding,name='index'),
  path('form',views.render_input,name= 'send-form'),
  path('advanced',views.render_testing,name="render testing")
]
