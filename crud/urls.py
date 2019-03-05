from django.urls import path, include

from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.CredentialList.as_view(), name='index'),
    path('create/', views.CredentialCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.CredentialDelete.as_view(), name='delete'),
    path('update/<int:pk>/', views.CredentialUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.CredentialDetail.as_view(), name='detail'),
]
