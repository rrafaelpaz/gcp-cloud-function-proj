
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rafael'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return "hello porra!"



