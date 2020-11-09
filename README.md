# Chakavak Dashboard

## What is this ?

This Project is for Monitor and Managing Services like SBC , RTP , SSW and ...  
for run project you new Run project in two part .  
Part 1 is chakavak-agent thats run on agent machine for send service status to Dashboard API .  
Part2 is Django-Dashboard that give information from chakavak-agent and fill service page with them information .  


## Run Project

The first thing to do is run Chakavak-Agent:

```sh
$ cd Chakava_Agent
$ python Chakavak_Agent.py
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies ( in main project Directory ):
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

Dashboard Rule List made from json file located in `config/json` that named rules.json 

Any rules should run special services that placed in json file located in `config/json` that named service_list.json . If any of those services are not runned, these rules will not be runned.

