# Susan Lin 
# SoftDev pd8
# K #13: Echo Echo Echo . . .
# 2018-09-28

from flask import Flask, render_template, request 
app = Flask(__name__)
       
@app.route('/')
def display():
    return render_template('form.html') 

@app.route('/auth')
def authenticate():
    return render_template('return.html',
                           user=request.args['in'],
                           method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
