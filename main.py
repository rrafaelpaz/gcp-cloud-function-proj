
#import logging
import subprocess
import os

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
    cmd = "python ./my-proxy/tools/deploy.py -n rafael_proxy -u rrafaelpaz@gmail.com:!Cranberries@2018 -o rrafaelpaz-eval -e test -d ./my-proxy -p /"
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
        '-u', 'rrafaelpaz@gmail.com:!Cranberries@2018',
        '-o', 'rrafaelpaz-eval',
        '-e', 'test',
        '-d', cwd,
        '-p', '/'])

        output.wait()

    except:
        print(output)    
    
    return output  

def directoryApp():
    return os.getcwd()

#@app.route('/test3')
def test3(request):
    cwd = os.getcwd() + "/my-proxy"
    deploy = os.getcwd() + "/my-proxy/deploy.py"
    cmd = "python "+deploy+" -n rafael_proxy -u rrafaelpaz@gmail.com:!Cranberries@2018 -o rrafaelpaz-eval -e test -d "+ cwd +" -p /"
    p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=False)
    output = b''.join(p.stdout).decode('utf-8')
    #return subprocess.check_call(["./my-proxy/tools/deploy.py", 'rafael_proxy', 'rrafaelpaz@gmail.com:!Cranberries@2018', 'rrafaelpaz-eval', 'test', './my-proxy', '/' ])
    return output
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
