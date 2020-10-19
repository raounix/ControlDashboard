import ast
# Create your views here.
import json
import os
import subprocess
import sys

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import Service, SoftSwitch , SBC


def MainDashboardPage(request):
    input_file = open ('config/json/service_names.json')
    json_array = json.load(input_file)
    input_file.close()

    return render(request,"Dashboard_Templates/dash_base.html",json_array)




def MonitoringService(request,slug):
    if(slug=="ssw"):
        main=Service.objects.filter(Type="ssw")
        input_file = open ('config/json/service_names.json')
        json_array = json.load(input_file)
        input_file.close()
    #    print(main.service_id)
    #    b=SoftSwitch(service_id=main)
    #    b.save()
        return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"ssw"})
    elif(slug=="sbc"):
        main=Service.objects.filter(Type="sbc")
       
    #    print(main.service_id)
    #    b=SoftSwitch(service_id=main)
    #    b.save()
        return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"sbc"})





def AddService(request):
    if(request.POST['type']=="ssw"):
        Type=str(request.POST['type'])
        name=str(request.POST['name'])
        ip=str(request.POST['ip'])
        service_object=Service(name=name,Type=Type,ip=ip)
        service_object.save()
        ssw_object=SoftSwitch(service_id=service_object)
        ssw_object.save()


        return HttpResponse("ok")

    elif(request.POST['type']=="sbc"):
        print("ok")
        Type=str(request.POST['type'])
        name=str(request.POST['name'])
        ip=str(request.POST['ip'])
        service_object=Service(name=name,Type=Type,ip=ip)
        service_object.save()
        sbc_object=SBC(service_id=service_object)
        sbc_object.save()
        return HttpResponse("ok")

def EditService(request):

    serivce_id=request.POST['id']    
    new_name=request.POST['new_name']
    new_ip=request.POST['new_ip']

    edit_model = Service.objects.get(pk=serivce_id)
    edit_model.name=new_name
    edit_model.ip=new_ip
    edit_model.save()
    main=Service.objects.filter(Type="ssw")
    return HttpResponse("ok")



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
