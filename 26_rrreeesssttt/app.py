# Susan Lin
# SoftDev pd8
# K #25: Getting More REST
# 2018-11-15

from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request as request
import json, ssl

app = Flask(__name__)
context = ssl._create_unverified_context()

#home root
@app.route('/', methods=["POST", "GET"])
def home():

    #currencylayer ()
    URL_ONE = 'http://apilayer.net/api/live?access_key=7f1092d7f907a899bb7d6196216bf2fa&currencies=USD,BRL,BTC,KRW,CNY,NZD&format=1'
    response = request.urlopen(URL_ONE).read()
    info = json.loads(response)
    finalSource = info['source']
    finalInfo = info['quotes']


    #xkcd (Theodore Peters)
    URL_TWO = 'http://xkcd.com/info.0.json'
    response = request.urlopen(URL_TWO).read()
    info = json.loads(response)
    finalImage = info['img']

    #Advice Slip (Daniel Gelfand)
    URL_THREE = 'https://api.adviceslip.com/advice'
    response = request.urlopen(URL_THREE).read()
    info = json.loads(response)
    finalAdvice = info['slip']['advice']

    return render_template("index.html", context=context, source=finalSource, curr=finalInfo, image=finalImage, advice=finalAdvice)

if __name__ == "__main__":
    app.debug = True
    app.run()
