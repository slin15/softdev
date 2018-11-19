# Susan Lin
# SoftDev pd8
# K #25: Getting More REST
# 2018-11-15

from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request as request
import json, requests

app = Flask(__name__)

headers = {'authorization': 'TYcbepeTSXWW2wm3eJKGsipKGjjKy45Vn7y6XD7SDzrgeNPH09rbF'}

#home root
@app.route('/', methods=["POST", "GET"])
def home():

    #currencylayer ()
    URL_ONE = 'https://public.enigma.com/api/collections/'   
    info = requests.get(URL_ONE, headers=headers).json()
    
    URL_TWO = 'https://public.enigma.com/api/datasets/' 
    info2 = requests.get(URL_TWO, headers=headers).json()
    a = []
    for item in info2: 
        if item['display_name'] < "Congress": 
            a.append(item)

    return render_template("index.html", info=info, info2=a)

if __name__ == "__main__":
    app.debug = True
    app.run()
