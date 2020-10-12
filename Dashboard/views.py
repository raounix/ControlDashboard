from django.shortcuts import render
import os,subprocess
# Create your views here.



def Index(request):
    return render(request,"Dashboard_Templates/index.html")




def MonitoringService(request):
    
    
    return render (request,"Dashboard_Templates/ServiceMonitoring.html",{'alldata':[{'name':'Nginx','status':'Up','uptime':'75'},{'name':'Apache','status':'Down','uptime':'50'}]})




def error_404(request,exception):
    return render(request, 'Dashboard_Templates/pages-404.html', status=404)