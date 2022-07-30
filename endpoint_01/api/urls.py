from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_users),
    path('add/', views.create_user),
    path('issue/', views.create_issue),
]
