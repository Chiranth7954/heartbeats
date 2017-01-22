# -*- coding: utf-8 -*-

from flask_oauth import OAuth


oauth = OAuth()

from credentials import *

from flask import session
from flask import Flask
from flask.ext.pymongo import PyMongo
import webbrowser

from makeSpotifyPlaylist import *
import algorithm
import os

app = Flask(__name__, static_url_path='')
mongo = PyMongo(app)

os.system('python algorithm.py')
spotifyOAuth(algorithm.uri_links)

@gFit.tokengetter
def get_gFit_token(token=None):
    print 'here\n'
    print session.get('gFit_token')

@app.route('/')
def hello():

    return 'success'

@app.route('/login')
def login():
    return gFit.authorize(callback='http://localhost:5000/login')

@app.route('/callback')
def callback():

    return '!!!!'


@app.route('/index')
def home_page():
    #online_users = mongo.db.users.find({'online': True})
    # return 'the index?'
    return app.send_static_file('index.html')
    #return render_template(('index.html'),online_users=online_users)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()
