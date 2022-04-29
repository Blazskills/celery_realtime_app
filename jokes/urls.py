from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vueapp', views.vueapp, name='vueapp')
    

]