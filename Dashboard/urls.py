from django.conf.urls import url
from django.urls import path

from Dashboard import views

urlpatterns=[
    path("",views.MainDashboardPage),
    path("<slug:slug>",views.MonitoringServer),
    # #  path('start-service/', views.StartService),
    # #  path('stop-service/',views.StopService),
    path('add-service/',views.AddServer),
    path('edit-service/',views.EditServer),
    path('deleting-service/',views.DeleteServer),

]

