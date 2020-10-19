from django.conf.urls import url
from django.urls import path

from Dashboard import views

urlpatterns=[
    path("",views.MainDashboardPage),
    path("<slug:slug>",views.MonitoringService),
    #  path('start-service/', views.StartService),
    #  path('stop-service/',views.StopService),
    path('add-service/',views.AddService),
    path('edit-service/',views.EditService),
   

]

