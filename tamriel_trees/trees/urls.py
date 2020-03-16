from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'trees'

urlpatterns = [
    path('createTree/', views.createTree, name='createTree'),

    path('mTree/<id>/', views.mTreeDetail, name='mTreeDetail'),
    path('mTree/<id>/addSkill', views.mAddSkill, name='mAddSkill'),
    path('mTree/<int:tree_id>/edit/<int:skill_id>', views.mEditSkill, name='mEditSkill'),
    path('mTree/<id>/clone', views.mCloneTree, name='mCloneTree'),
]