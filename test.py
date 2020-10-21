import requests

url = 'http://127.0.0.1:5000/start'
myjson = {'service_name': 'nordvpn','service_list':[{'name':"raouf"},{'name':"rasoul"}]}

x = requests.post(url, json = myjson)

#print the response text (the content of the requested file):

print(x.json)
