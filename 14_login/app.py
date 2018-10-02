# Team SillySquids : Robin Han and Susan Lin 
# SoftDev pd8
# K #14: Do I Know You?    this
# 2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)
#hard coded valid username and 
users = {"slin15": "12345"} 
       
#home root
@app.route('/', methods=["POST", "GET"])
def home():
     return render_template('form.html')
#reading in user and password, checking to see if it is valid or not
@app.route('/login', methods=["POST", "GET"])
def login():    
    if request.args['user'] in users.keys() and users[request.args['user']] == request.args['pass']:
	#username and passwords match         
	return render_template('return.html', user=request.args['user'], password=request.args['pass']) 
	    
    elif request.args['user'] not in users.keys():
        #username doesn't match
	return render_template('error.html', error="username not found")

    elif users[request.args['user']] != request.args['pass']:
	#password doesn't match username        
	return render_template('error.html', error="incorrect password")

# logout route, sends user back to home root and forgets current user
@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop['slin15'] 
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
