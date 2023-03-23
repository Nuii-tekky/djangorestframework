
from django.urls import path
from . import views

urlpatterns = [
  path('', views.renderlanding,name='index'),
  path('form',views.render_input,name= 'send-form'),
  path('advanced',views.render_testing,name="render testing"),
  path('newest',views.render_final_testing_1,name="testing5"),
  path('image',views.render_image_form,name="testing5"),
  path('getimage',views.render_get_image,name="getimage"),
  path('render-checker',views.render_checker,name="renderchecker"),
  path("render-dynamic",views.render_dynamic,name="renderdynamic"),
  path("desktop",views.render_desktop,name="desktop"),
  path("mobile",views.render_mobile,name="mobile"),
  path("multi",views.render_multitry,name="multitry"),
  path("all-words",views.render_all_words,name="renderallwords"),
  path("all-img",views.renderallimg,name="allimg")

]



