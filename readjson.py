import json
import os,subprocess
import collections
from django.core import serializers

def check_service_status(server,service_list):
    is_enable=True

    for service in service_list['rules'][server.Type]['service']:
        
            State=str(subprocess.Popen(["systemctl", "show", "-p", "SubState", "--value", service["name"]],stdout=subprocess.PIPE).communicate())


            if "running" in State or "exited" in State:
                pass
            else:
                is_enable=False

                
    return is_enable
        




def check_all_service(server_file):
    result=collections.defaultdict(dict)

    input_file = open ('config/json/service_list.json')
    json_array = json.load(input_file)
    input_file.close()    

    for server in server_file:
        status=check_service_status(server,json_array)
        result[server.name]['status'] =status
    
    result=dict(result)
    print(result)

        
        


