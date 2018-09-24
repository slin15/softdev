# Anton Danylenko and Susan Lin 
# SoftDev pd8
# K #10: Jinja Tuning ...
# 2018-09-24

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome <br> <a href="/occupations"> Occupations </a>'

@app.route('/occupations')
def test():
    return render_template('temp01.html',
                               title = "Occupations",
                               heading = "This file selects a random occupation from the table below and displays it at the top.")

if __name__ == "__main__":
    app.debug = True
    app.run()
