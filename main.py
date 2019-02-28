
import logging
from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/start')
def start(request):
    return "Function was triggered"


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
