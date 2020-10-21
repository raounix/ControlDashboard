import flask
import os
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"]=False



# @app.route('status',methods=['GET'])
# def Status(request) 

@app.route('/',methods=['POST'])
def StartService():

    try:
        

        return (request.form["test"])
        
        
    except:
        pass
    
    # service=str(request.POST['data'])
    # service=service.replace(".service","")
    # os.system("service "+service+" start")
    # return HttpResponse(request.POST['Success'])


# @app.route('/',methods=['GET'])
# def StopService(request):
#     service=str(request.POST['data'])
#     service=service.replace(".service","")
#     os.system("service "+service+" stop")
#     # return HttpResponse(request.POST['data'])


app.run()