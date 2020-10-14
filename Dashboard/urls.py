from django.urls import path
from Dashboard import views
from django.conf.urls import url
urlpatterns=[
    path("",views.MainDashboardPage),
    path("monitoring_service",views.MonitoringService),
    #  path('start-service/', views.StartService),
    #  path('stop-service/',views.StopService),


]

