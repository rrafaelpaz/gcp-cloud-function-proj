
import logging
import subprocess
from subprocess import call
from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/start')
def start():
    return "Function was triggered"

@app.route('/deploy')
def deploy():
    return subprocess.check_output(["echo", "Hello World!"])    


@app.route('/test')
def test(request):
    command = "python ./my-proxy/tools/deploy.py -n rafael_proxy -u rrafaelpaz@gmail.com:!Cranberries@2018 -o rrafaelpaz-eval -e test -d ./my-proxy -p /"
    subprocess.Popen(command, shell=True)
    return "Proxy deployed to Apigee"  

def deploy2(request):
    proxy_name = os.environ.get('PROXY_NAME', None)
    user_name = os.environ.get('USER_NAME', None)
    password = os.environ.get('PASSWORD', None)
    org = os.environ.get('ORG', None)
    env = os.environ.get('ENV', None)
    command = "python ./my-proxy/tools/deploy.py -n" + proxy_name + " -u "+ user_name + ":"+ password + " -o "+ org +" -e "+ env +" -d ./my-proxy -p /"
    subprocess.Popen(command, shell=True)
    return "Proxy deployed to Apigee" 


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
