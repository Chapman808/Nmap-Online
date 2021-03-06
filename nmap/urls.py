from django.urls import path

from . import views
from .views import SubmitNmap
urlpatterns = [
    path('', views.index, name='nmap'),
    path('api/submit/', SubmitNmap.as_view(), name='api/submit/'),
    path('api/scans/', views.getHostScansAsJson, name='api/scans/')
]