from django.conf.urls import url

from elevate import views


urlpatterns = [
    url(r'^elevate/', views.elevate, name='elevate'),
]
