import flask
import os
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"]=False



# @app.route('status',methods=['GET'])
# def Status(request) 

@app.route('/start',methods=['POST'])
def StartService():

    try:
        service=request.json['service_name']
        # os.system("service "+service+" start")
        print(request.json['service_list'][1]['name'])
        return (request.json)
        
        
    except:
        return("fail")
    


@app.route('/stop',methods=['POST'])
def StopService():
        service=request.json['service_name']
        os.system("service "+service+" stop")
        return("ok")
        # return HttpResponse(request.POST['data'])

def GetAllStatus():
        pass

app.run()


    # service=str(request.POST['data'])
    # service=service.replace(".service","")
    
    # return HttpResponse(request.POST['Success'])
