import ast
# Create your views here.
import json
import os
import subprocess
import sys
import requests
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Server,SSWConfig,SBCConfig,RTPConfig,SSW,SBC,RTP


###################################################################################################

###################################################################################################



def MainDashboardPage(request):
    input_file = open ('config/json/rules.json')
    json_array = json.load(input_file)
    input_file.close()

    return render(request,"Dashboard_Templates/dash_base.html",{"all":json_array})



###################################################################################################

###################################################################################################




def MonitoringServer(request,slug):
    try : 
        if(slug=="all-service"):
            main=Server.objects.all()
            input_file = open ('config/json/rules.json')
            json_array = json.load(input_file)
            input_file.close()
            status={}
            for server in main:
                data={'name':server.server_id,'type':server.Type}
                r=requests.post(url="http://127.0.0.1:5000/check-status",json=data)
                status[server.name]=r.text
            
            
            return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"all","all":json_array,'status':status})


        elif(slug=="ssw"):
            status={}
            main=Server.objects.filter(Type="ssw")
            input_file = open ('config/json/rules.json')
            json_array = json.load(input_file)
            input_file.close()
      
            
            for server in main:
                data={'name':server.server_id,'type':server.Type}
                r=requests.post(url="http://127.0.0.1:5000/check-status",json=data)
                status[server.name]=r.text
    
            return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"ssw","all":json_array,'status':status})
            

        elif(slug=="sbc"):
            status={}
            main=Server.objects.filter(Type="sbc")
            input_file = open ('config/json/rules.json')
            json_array = json.load(input_file)
            input_file.close()



            for server in main:
                data={'name':server.server_id,'type':server.Type}
                r=requests.post(url="http://127.0.0.1:5000/check-status",json=data)
                status[server.name]=r.text
            return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"sbc","all":json_array,'status':status})


        elif(slug=="rtp"):
            status={}
            main=Server.objects.filter(Type="rtp")
            input_file = open ('config/json/rules.json')
            json_array = json.load(input_file)
            input_file.close()



            for server in main:
                data={'name':server.server_id,'type':server.Type}
                r=requests.post(url="http://127.0.0.1:5000/check-status",json=data)
                status[server.name]=r.text
            return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"rtp","all":json_array,'status':status})


        else:
            return render(request,"Dashboard_Templates/404.html")
    except:
        return HttpResponse("error")



###################################################################################################

###################################################################################################

## Edit Server Info


def AddServer(request):
    try:
        if(request.POST['type']=="ssw"):
            Type=str(request.POST['type'])
            name=str(request.POST['name'])
            ip=str(request.POST['ip'])
            server_object=Server(name=name,Type=Type,ip=ip)
            server_object.save()
            ssw_object=SSW(server_id=server_object)
            ssw_object.save()
            return HttpResponse("ok")


        elif(request.POST['type']=="sbc"):
            Type=str(request.POST['type'])
            name=str(request.POST['name'])
            ip=str(request.POST['ip'])
            server_object=Server(name=name,Type=Type,ip=ip)
            server_object.save()
            sbc_object=SBC(server_id=server_object)
            sbc_object.save()
            return HttpResponse("ok")


        elif(request.POST['type']=="rtp"):
            Type=str(request.POST['type'])
            name=str(request.POST['name'])
            ip=str(request.POST['ip'])
            server_object=Server(name=name,Type=Type,ip=ip)
            server_object.save()
            rtp_object=RTP(server_id=server_object)
            rtp_object.save()


            return HttpResponse("ok")
        
    except:
        return HttpResponse("error")



###################################################################################################

###################################################################################################




def EditServer(request):
    try:
        server_id=request.POST['id']    
        new_name=request.POST['new_name']
        new_ip=request.POST['new_ip']

        edit_model = Server.objects.get(pk=server_id)
        edit_model.name=new_name
        edit_model.ip=new_ip
        edit_model.save()
        return HttpResponse("ok")
    except:
        return HttpResponse("error")

###################################################################################################

###################################################################################################





def DeleteServer(request):
    
    try:
        server_id=request.POST['id']
        Server.objects.filter(pk=server_id).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse("error")





###################################################################################################
## END OF Edit Server Info
###################################################################################################

## Get Info From Server



def start_server_service(request):
    try:
        Type=request.POST['type']
        ip=request.POST['ip']
        payload={'type':Type}
        response = requests.post('http://'+ip+':5000/start-server',json=payload)


        return HttpResponse("ok")
    except:
        return HttpResponse("fail")

###################################################################################################

###################################################################################################






def stop_server_service(request):
    try:
        Type=request.POST['type']
        ip=request.POST['ip']
        payload={'type':Type}
        response = requests.post('http://'+ip+':5000/stop-server',json=payload)


        return HttpResponse("ok")
    except:
        return HttpResponse("fail")
###################################################################################################

###################################################################################################




def start_subservice(request):
    try:
        SubServiceName=request.POST['subservice']
        ip=request.POST['ip']
        payload={'subservice':SubServiceName}
        response = requests.post('http://'+ip+':5000/start-subservice',json=payload)


        return HttpResponse("ok")
    except:
        return HttpResponse("fail")

###################################################################################################

###################################################################################################






def stop_subservice(request):
    try:
        SubServiceName=request.POST['subservice']
        ip=request.POST['ip']
        payload={'subservice':SubServiceName}
        response = requests.post('http://'+ip+':5000/stop-subservice',json=payload)


        return HttpResponse("ok")
    except:
        return HttpResponse("fail")

###################################################################################################

###################################################################################################


def status_subservice(request):
    try:
        if(request.method=='GET'):

            ip=request.GET['ip']
            Type=request.GET['type']
            payload = {'type':Type}
            response = requests.get('http://'+ip+':5000/status-subservice', params=payload)
            data=json.loads(response.content)
            return JsonResponse(data=data)
      

    except:
            return HttpResponse("fail")



###################################################################################################
## END OF  Get Info From Server
###################################################################################################
