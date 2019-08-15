from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sith', views.sith, name='sith'),
    path('recruit', views.recruit, name='recruit'),
    path('requests', views.requests, name='requests'),
    path('shadow_hand', views.shadow_hand, name='shadow_hand'),
]
