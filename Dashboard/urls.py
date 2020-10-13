from django.urls import path
from Dashboard import views
from django.conf.urls import url
urlpatterns=[
    path("",views.Index),
    path("monitoring_service",views.MonitoringService),
     path('my-ajax-test/', views.testcall),


]

