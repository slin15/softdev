# Team SillySquids : Robin Han and Susan Lin 
# SoftDev pd8
# K #14: Do I Know You?    this
# 2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)
users = {"slin15": "12345"} 
       
@app.route('/', methods=["POST", "GET"])
def home():
     return render_template('form.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.args['username'] in users.keys() and users[user] == request.args['password']:
         return render_template('return.html', user = 'slin15') 
    
    elif request.args['username'] not in users.keys():
        return render_template('error.html', error = "username not found")

    elif users[request.args['username']] != request.args['password']:
        return render_template('error.html', error = "incorrect password")
    else:
        return render_template('form.html')

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop['slin15'] 
    return render_template('form.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
