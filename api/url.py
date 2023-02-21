from django.urls import path
from . import views


urlpatterns= [
  path('my-very-first-endpoint/<str:name>', views.view_by_name,name='first-api-response'),
  path('send-post-data',views.add_data,name= 'post-data')
]

