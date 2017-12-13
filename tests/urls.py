from django.conf.urls import url
import django

from elevate import views

if django.VERSION[:3] >= (1, 9, 0):

    urlpatterns = [
        url(r'^elevate/', views.elevate, name='elevate'),
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        url(r'^elevate/', 'elevate.views.elevate', name='elevate'),
    )
