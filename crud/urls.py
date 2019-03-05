
from django.urls import path, include

from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/(?P<id>\d+)/', views.delete, name='delete'),
    path('update/(?P<id>\d+)/', views.update, name='update'),
    path('detail/(?P<id>\d+)/', views.detail, name='detail'),
]
