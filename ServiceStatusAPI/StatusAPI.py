import json
import os,subprocess
import collections
import flask
import requests
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from flask import request, jsonify




app = flask.Flask(__name__)
app.config["DEBUG"]=False
app.config['CORS_HEADERS'] = 'Content-Type'


#########################################################################################

def check_service_status(Type):
    is_enable=True
    input_file = open ('../config/json/service_list.json')
    service_list = json.load(input_file)
    input_file.close()
    for service in service_list['rules'][Type]['service']:
            State=str(subprocess.Popen(["systemctl", "show", "-p", "SubState", "--value", service["name"]],stdout=subprocess.PIPE).communicate())


            if "running" in State or "exited" in State:
                pass
            else:
                is_enable=False

                
    return is_enable

#########################################################################################

#########################################################################################

def start_server(Type):
    input_file = open ('../config/json/service_list.json')
    service_list = json.load(input_file)
    input_file.close()
    for service in service_list['rules'][Type]['service']:
            os.system("service "+ service['name'] + " start")


#########################################################################################

#########################################################################################


                
def stop_server(Type):
    input_file = open ('../config/json/service_list.json')
    service_list = json.load(input_file)
    input_file.close()
    for service in service_list['rules'][Type]['service']:
            os.system("service "+ service['name'] + " stop")

#########################################################################################

#########################################################################################

def start_subservice(SubService):


    os.system("service "+ SubService + " start")


#########################################################################################

#########################################################################################


                
def stop_subservice(SubService):

    os.system("service "+ SubService + " stop")



#########################################################################################

#########################################################################################


def check_subservice_status(Type):
    data={}
    input_file = open ('../config/json/service_list.json')
    service_list = json.load(input_file)
    input_file.close()
    for service in service_list['rules'][Type]['service']:
            State=str(subprocess.Popen(["systemctl", "show", "-p", "SubState", "--value", service["name"]],stdout=subprocess.PIPE).communicate())


            if "running" in State or "exited" in State:
                data[service["name"]]="start"
            else:
                data[service["name"]]="stop"

                
    return data


                
#########################################################################################

#########################################################################################

#########################################################################################

## Routing Section



@app.route('/check-status',methods=['POST'])
def CheckStatus_handling():
    try:
        Type=request.json['type']
        is_enable=check_service_status(Type)
        if(is_enable==True):
            return "enable"
        else:
            return "disable"
    except:
        return "error"
#########################################################################################


@app.route('/status-subservice',methods=['GET'])
def subservice_status_handling():
    try:
        Type=request.args.get('type')
        data=check_subservice_status(Type)
        response = flask.jsonify(data)

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except:
        return "error"


#########################################################################################

@app.route('/start-server',methods=['POST'])
def start_server_handling():
    try:
        Type=request.json['type']
        start_server(Type)
        return "ok"

    except:
        return "error"

#########################################################################################


@app.route('/stop-server',methods=['POST'])
def stop_server_handling():
    try:
        Type=request.json['type']
        
        stop_server(Type)
        return "ok"

    except:
        return "error"
    #########################################################################################



@app.route('/start-subservice',methods=['POST'])
def start_subservice_handling():
    try:
        SubServName=request.json['subservice']
        start_subservice(SubServName)
        
        return "ok"
    except:
        return "error"

#########################################################################################


@app.route('/stop-subservice',methods=['POST'])
def stop_subservice_handling():
    try:
        SubServName=request.json['subservice']
        stop_subservice(SubServName)
        return "ok"

    except:
        return "error"


#########################################################################################

app.run()


