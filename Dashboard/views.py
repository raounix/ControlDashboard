from django.shortcuts import render
import os,subprocess,sys,subprocess
from django.http import HttpResponse
# Create your views here.
import json

import ast


def MainDashboardPage(request):
    input_file = open ('config/json/service_names.json')
    json_array = json.load(input_file)
    input_file.close()

    return render(request,"Dashboard_Templates/index.html",json_array)




def MonitoringService(request):
   pass



def StartService(request):
    service=str(request.POST['data'])
    service=service.replace(".service","")
    os.system("service "+service+" start")
    # return HttpResponse(request.POST['Success'])

def StopService(request):
    service=str(request.POST['data'])
    service=service.replace(".service","")
    os.system("service "+service+" stop")
    # return HttpResponse(request.POST['data'])
