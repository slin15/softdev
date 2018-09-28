# Anton Danylenko and Susan Lin 
# SoftDev pd8
# K #10: Jinja Tuning ...
# 2018-09-24

from util import occupations 

from flask import Flask, render_template
app = Flask(__name__)
       
@app.route('/')
def home():
    return 'Welcome <br> <a href="/auth"> Returning... </a>'

@app.route('/auth')
def test():
    return render_template('temp01.html',
                               title = "",
                               heading = "")

if __name__ == "__main__":
    app.debug = True
    app.run()
