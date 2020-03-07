from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('trees/', include('trees.urls')),
]
