import ast
# Create your views here.
import json
import os
import subprocess
import sys
import requests
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.forms.models import model_to_dict
from .models import Server,SSW_SIPProfile,SBCConfig,RTPConfig,SSW,SBC,RTP


###################################################################################################

###################################################################################################

def Login(request):
    if(request.user.is_authenticated ==False):

        if(request.method=="POST"):
            try:
                username=request.POST['username']
                password=request.POST['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            except:
                return redirect('/login/')
            # return render(request,"Dashboard_Templates/login.html",{"login_status":"not_login"})
        else:
            return render(request,"Dashboard_Templates/login.html")
    else:
        return redirect('/')
        

###################################################################################################

###################################################################################################


def Logout(request):
    if(request.user.is_authenticated ):

        if(request.method=="GET"):
          
                logout(request)

                return redirect('/login/')

            # return render(request,"Dashboard_Templates/login.html",{"login_status":"not_login"})
        else:
            return render(request,"Dashboard_Templates/login.html")
    else:
        return redirect('/')

###################################################################################################

###################################################################################################


def MainDashboardPage(request):
    if(request.user.is_authenticated ):

        input_file = open ('config/json/rules.json')
        json_array = json.load(input_file)
        input_file.close()
        ssw_data=Server.objects.filter(Type="ssw")

        return render(request,"Dashboard_Templates/dash_base.html",{"all":json_array,"ssw_data":ssw_data})
    else:
        return redirect('/login/')



###################################################################################################

###################################################################################################


def SIP_Profile_Handler(request,slug):
    if(request.user.is_authenticated ):
        id_list=set({})
        sip_profile_id=dict({})
        input_file = open ('config/json/rules.json')
        json_array = json.load(input_file)
        input_file.close()
        ssw_data=Server.objects.filter(Type="ssw")
        server_id=Server.objects.filter(Type="ssw",name=slug).values('server_id')[0]['server_id']
        SipProfile_ssw=SSW.objects.filter(server_id=server_id).values('SipProfile')
        
        for it in SipProfile_ssw:
                id_list.add(it['SipProfile'])
        
        for it in id_list:
            key=SSW_SIPProfile.objects.filter(pk=it)
            value=SSW_SIPProfile.objects.filter(pk=it).values('Profile_Name')
            

            sip_profile_id[it]=value[0]['Profile_Name']

        
        return render(request,"Dashboard_Templates/config_profile.html",{"all":json_array,"ssw_data":ssw_data,'sip_profile':sip_profile_id})
        

    else:
        return redirect('/login/')


###################################################################################################

###################################################################################################

def CreateSipProfileXml(request):
    json_body={'profile_name':'',
    'params':[ 
    ]
    }
    
    inject_body={}
    counter=int(request.POST['count'])
    json_body['profile_name']=request.POST['value_id']
    
    for i in range(counter):
        inject_body={}
        inject_body['name']=request.POST["name_"+str(i+1)]
        inject_body['value']=request.POST["value_"+str(i+1)]
        
        json_body['params'].append(inject_body)
    
    requests.post(url="http://127.0.0.1:5001/profile",json=json_body)
    return HttpResponse(request.POST['count'])

###################################################################################################

###################################################################################################

def MonitoringServer(request,slug):
    if(request.user.is_authenticated ):
        try : 
            if(slug=="all-service"):
                main=Server.objects.all()
                input_file = open ('config/json/rules.json')
                json_array = json.load(input_file)
                input_file.close()
                ssw_data=Server.objects.filter(Type="ssw")
                status={}
                try:
                    for server in main:
                        data={'name':server.server_id,'type':server.Type}
                        r=requests.post(url="http://"+server.ip+":5000/check-status",json=data)
                        status[server.name]=r.text
            
                
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"all","all":json_array,'status':status,"ssw_data":ssw_data})
                except:
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":'',"type":"all","all":json_array,'status':'',"ssw_data":ssw_data})


            elif(slug=="ssw"):
                status={}
                main=Server.objects.filter(Type="ssw")
                input_file = open ('config/json/rules.json')
                json_array = json.load(input_file)
                input_file.close()
                ssw_data=Server.objects.filter(Type="ssw")
                try:
                    for server in main:
                        data={'name':server.server_id,'type':server.Type}
                        r=requests.post(url="http://"+server.ip+":5000/check-status",json=data)
                        status[server.name]=r.text
        
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"ssw","all":json_array,'status':status,"ssw_data":ssw_data})
                except:
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":'',"type":"ssw","all":json_array,'status':'',"ssw_data":ssw_data})
            

            elif(slug=="sbc"):
                status={}
                main=Server.objects.filter(Type="sbc")
                input_file = open ('config/json/rules.json')
                json_array = json.load(input_file)
                input_file.close()
                ssw_data=Server.objects.filter(Type="ssw")


                try:
                    for server in main:
                        data={'name':server.server_id,'type':server.Type}
                        r=requests.post(url="http://"+server.ip+":5000/check-status",json=data)
                        status[server.name]=r.text
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"sbc","all":json_array,'status':status,"ssw_data":ssw_data})
                except:
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":'',"type":"sbc","all":json_array,'status':'',"ssw_data":ssw_data})
                

            elif(slug=="rtp"):
                status={}
                main=Server.objects.filter(Type="rtp")
                input_file = open ('config/json/rules.json')
                json_array = json.load(input_file)
                input_file.close()
                ssw_data=Server.objects.filter(Type="ssw")


                try:
                    for server in main:
                        data={'name':server.server_id,'type':server.Type}
                        r=requests.post(url="http://"+server.ip+":5000/check-status",json=data)
                        status[server.name]=r.text
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":main,"type":"rtp","all":json_array,'status':status,"ssw_data":ssw_data})
                except:
                    return render(request,"Dashboard_Templates/datatable.html",{"alldata":'',"type":"rtp","all":json_array,'status':'',"ssw_data":ssw_data})

            
            else:
                return render(request,"Dashboard_Templates/404.html")
        except:
            return HttpResponse("error")
    else:
        return redirect("/login/")


###################################################################################################

###################################################################################################

## Edit Server Info


def AddServer(request):
    if(request.user.is_authenticated ):

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
    else:
        return redirect("/login/")



###################################################################################################

###################################################################################################




def EditServer(request):
    if(request.user.is_authenticated ):
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
    else:
        return redirect("/login/")

###################################################################################################

###################################################################################################





def DeleteServer(request):
    if(request.user.is_authenticated ):
        try:
            server_id=request.POST['id']
            Server.objects.filter(pk=server_id).delete()
            return HttpResponse("ok")
        except:
            return HttpResponse("error")
    else:
        return redirect("/login/")




###################################################################################################
## END OF Edit Server Info
###################################################################################################

## Get Info From Server



def start_server_service(request):
    if(request.user.is_authenticated ):
        try:
            Type=request.POST['type']
            ip=request.POST['ip']
            payload={'type':Type}
            response = requests.post('http://'+ip+':5000/start-server',json=payload)


            return HttpResponse("ok")
        except:
            return HttpResponse("fail")
    else:
        return redirect("/login/")
###################################################################################################

###################################################################################################






def stop_server_service(request):
    if(request.user.is_authenticated ):
        try:
            Type=request.POST['type']
            ip=request.POST['ip']
            payload={'type':Type}
            response = requests.post('http://'+ip+':5000/stop-server',json=payload)


            return HttpResponse("ok")
        except:
            return HttpResponse("fail")
    else:
        return redirect('/login/')
###################################################################################################

###################################################################################################




def start_subservice(request):
    if(request.user.is_authenticated ):
        try:
            SubServiceName=request.POST['subservice']
            ip=request.POST['ip']
            payload={'subservice':SubServiceName}
            response = requests.post('http://'+ip+':5000/start-subservice',json=payload)


            return HttpResponse("ok")
        except:
            return HttpResponse("fail")
    else:
        return redirect("/login/")
###################################################################################################

###################################################################################################






def stop_subservice(request):
    if(request.user.is_authenticated ):
        try:
            SubServiceName=request.POST['subservice']
            ip=request.POST['ip']
            payload={'subservice':SubServiceName}
            response = requests.post('http://'+ip+':5000/stop-subservice',json=payload)


            return HttpResponse("ok")
        except:
            return HttpResponse("fail")
    else:
        return redirect("/login/")
###################################################################################################

###################################################################################################


def status_subservice(request):
    if(request.user.is_authenticated ):
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
    else:
        return redirect("/login/")


###################################################################################################
## END OF  Get Info From Server
###################################################################################################
