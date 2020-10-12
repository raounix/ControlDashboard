from django.urls import path
from Dashboard import views
from django.conf.urls import url,handler404
urlpatterns=[
    path("",views.Index),
    path("monitoring_service",views.MonitoringService),


]
handler404 = 'Dashboard.views.error_404'
