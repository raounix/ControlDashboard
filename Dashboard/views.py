from django.shortcuts import render
import os,subprocess,sys,subprocess
# Create your views here.
import json

import ast


def Index(request):
    return render(request,"Dashboard_Templates/index.html")




def MonitoringService(request):
    input_file = open ('config/json/service_names.json')
    json_array = json.load(input_file)

    elements={}
    json_builder={"alldata": []}

    
    for service_name in json_array["service"]:
        
        
        
        State=str(subprocess.Popen(["systemctl", "show", "-p", "SubState", "--value", service_name["name"]],stdout=subprocess.PIPE).communicate())
        
    
        if "running" in State or "exited" in State:
            elements[service_name["name"]]="Up"
        else:
            elements[service_name["name"]]="Down"
        
        


    json_builder["alldata"].append((elements))

    
    return render (request,"Dashboard_Templates/ServiceMonitoring.html",json_builder)




def error_404(request,exception):
    return render(request, 'Dashboard_Templates/pages-404.html', status=404)