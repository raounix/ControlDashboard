from django.conf.urls import url
from django.urls import path

from Dashboard import views

urlpatterns=[
    path("",views.MainDashboardPage),
    path("<slug:slug>",views.MonitoringServer),
    path('start-service/',views.start_server_service),
    path('stop-service/',views.stop_server_service),
    path('status-subservice/',views.status_subservice),
    path('add-service/',views.AddServer),
    path('edit-service/',views.EditServer),
    path('deleting-service/',views.DeleteServer),
    path('start-subservice/',views.start_subservice),
    path('stop-subservice/',views.stop_subservice),

]

