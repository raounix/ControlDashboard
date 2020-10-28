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


## Routing Section



@app.route('/check-status',methods=['POST'])
def CheckStatus():
    Type=request.json['type']
    is_enable=check_service_status(Type)
    if(is_enable==True):
        return "enable"
    else:
        return "disable"

#########################################################################################

#########################################################################################

@app.route('/status-subservice',methods=['GET'])
def subservice_status():
    Type=request.args.get('type')
    data=check_subservice_status(Type)
    response = flask.jsonify(data)

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

      
# @app.route('/stop',methods=['POST'])
# def check_all_service(server_file):
#     result=collections.defaultdict(dict)

#     input_file = open ('config/json/service_list.json')
#     json_array = json.load(input_file)
#     input_file.close()

#     for server in server_file:
#         status=check_service_status(server,json_array)
#         result[server.name]['status'] =status
    
#     result=dict(result)
#     print(result)  



app.run()



