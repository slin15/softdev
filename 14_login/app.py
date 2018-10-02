# Team SillySquids : Robin Han and Susan Lin 
# SoftDev pd8
# K #14: Do I Know You?    this
# 2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32) 
       
@app.route('/', methods=["GET"])
def disp_login():
    return render_template('form.html') 

@app.route('/auth')
def authenticate():
    print (url_for('disp_login'))
    print (url_for('authenticate'))
    return (redirect(url_for('disp_login')))
    #return render_template('return.html',
    #                       user=request.args['in'],password = request.args['pa$
    #                      method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
