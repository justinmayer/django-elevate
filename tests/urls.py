from django.urls import re_path

from elevate import views


urlpatterns = [
    re_path(r'^elevate/', views.elevate, name='elevate'),
]
