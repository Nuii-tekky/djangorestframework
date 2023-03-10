from django.urls import path
from . import views


urlpatterns= [

  # students data 

  path('my-very-first-endpoint/<str:name>', views.view_by_name,name='first-api-response'),
  path('send-post-data',views.add_data,name= 'post-data'),
  path('update-data/<int:id>',views.update_data,name="update students"),


  # words

  path('my-endpoint/<int:id>', views.view_word,name='view-word-response'),
  path('send-word',views.add_word,name= 'post-word'),
  path('update-word/<int:id>',views.changeword,name= "change_word"),

  # images

  path("upload-image",views.add_image,name= "add_image"),
  path("view-image/<str:title>",views.get_image,name= "view_image")
]





