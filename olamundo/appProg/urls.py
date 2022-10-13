from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('checkin/', views.checkin, name='checkin')
]