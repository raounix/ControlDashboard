from django.shortcuts import render
import os,subprocess,sys,subprocess
from django.http import HttpResponse
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



def testcall(request):
    service=str(request.POST['data'])
    service=service.replace(".service","")
    # subprocess.Popen(["service", service, "stop" , "> /dev/null"],stdout=subprocess.PIPE).communicate()
    os.system("service "+service+" stop")
    return HttpResponse(request.POST['data'])