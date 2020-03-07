from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'trees'

urlpatterns = [
    path('createTree/', views.createTree, name='createTree'),
    path('tree/<id>/', views.treeDetail, name='treeDetail'),
    path('tree/<id>/addSkill', views.addSkill, name='addSkill'),
]