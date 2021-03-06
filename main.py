
#import logging
import subprocess
import os
import time

from flask import Flask, render_template, request
from flask import Flask



app = Flask(__name__)

#@app.route('/start')
def start():
    return "Function was triggered"

#@app.route('/deploy')
def Hello(request):
    return subprocess.check_output(["echo", "Hello World!"])  

    


#@app.route('/test2')
def test2(request):
    cmd = "python ./my-proxy/tools/deploy.py -n rafael_proxy -u myEmail:myPassw -o rrafaelpaz-eval -e test -d ./my-proxy -p /"
    # no block, it start a sub process.
    p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # and you can block util the cmd execute finish
    p.wait()
    # or stdout, stderr = p.communicate()
    return "Proxy deployed to Apigee"  

#@app.route('/test')
def test(request):
    output = None
    cwd = os.getcwd() + "/my-proxy"
    deploy = os.getcwd() + "/my-proxy/deploy.py"
   
    try:
        output = subprocess.check_output([
        deploy, 
        '-n',  'rafael_proxy',
        '-u', 'myEmail:myPassw',
        '-o', 'rrafaelpaz-eval',
        '-e', 'test',
        '-d', cwd,
        '-p', '/'])

        output.wait()

    except:
        print(output)    
    
    return output  


def directoryApp(request):
    return os.getcwd()

#@app.route('/test3')
def test3(request):
    cwd = os.getcwd() + "/my-proxy"
    deploy = os.getcwd() + "/my-proxy/deploy.py"
    cmd = "python "+deploy+" -n rafael_proxy -u myEmail:myPassw -o rrafaelpaz-eval -e test -d "+ cwd +" -p /"
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = output.communicate()
    output = b''.join(p.stdout).decode('utf-8')
    #return subprocess.check_call(["./my-proxy/tools/deploy.py", 'rafael_proxy', 'myEmail:myPassw', 'rrafaelpaz-eval', 'test', './my-proxy', '/' ])
    return output

    
#@app.route('/send')
def send(request):
    command = 'curl -X POST -u myEmail:myPassw  -F "file=@apiproxy.zip" "https://api.enterprise.apigee.com/v1/organizations/rrafaelpaz-eval/apis?action=import&name=example"'
    output=None
    try:
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = output.communicate()
    except:
        print(output)
    return output

@app.route('/deploy2')
def deploy2():
    deploy_file = os.getcwd() + "/deploy.py"
    deploy = os.getcwd() + "/my-proxy/deploy.py"

    command = 'openapi2apigee generateApi petStore -s /Users/rafaelpaz/Documents/python/mapping-api_0.0.3.yml -d /Users/rafaelpaz/Documents/python -D'
    output=None
    try:
        output = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        time.sleep(2.0)
        subprocess.Popen.kill(output)
        output = subprocess.check_output([
        deploy_file, 
        '-n', 'rafael_proxy',
        '-u', 'myEmail:myPassw',
        '-o', 'rrafaelpaz-eval',
        '-e', 'test',
        '-d', '/Users/rafaelpaz/Documents/python/petStore',
        '-p', '/'])
        output.wait()
        
    except:
        print(output)
    return output 

#@app.route('/send')
def send2():
    p = None
    try:
        command = 'curl -X POST -u myEmail:myPassw  -F "file=@apiproxy.zip" "https://api.enterprise.apigee.com/v1/organizations/rrafaelpaz-eval/apis?action=import&name=example"'
        p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # and you can block util the cmd execute finish
        p.wait()
    except:
        print(p)    
    
    return p    
    
def deploy2():
    proxy_name = os.environ.get('PROXY_NAME', None)
    user_name = os.environ.get('USER_NAME', None)
    password = os.environ.get('PASSWORD', None)
    org = os.environ.get('ORG', None)
    env = os.environ.get('ENV', None)
    command = "python ./my-proxy/tools/deploy.py -n" + proxy_name + " -u "+ user_name + ":"+ password + " -o "+ org +" -e "+ env +" -d ./my-proxy -p /"
    return subprocess.Popen(command, shell=True)
    

#@app.errorhandler(500)
#def server_error(e):
#    logging.exception('An error occurred during a request.')
#    return 'An internal error occurred.', 500
