# Susan Lin 
# SoftDev1 pd8
# K08 -- Fill Yer Flask
# 2018-09-20  

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign function to route
def home():
    return 'Hello <br> <br> <a href="/i"> I </a> <br> <a href="/ii"> II </a>' 

@app.route("/i") #assign function to route
def pt1():
    return '<a href="/"> HOME </a> <a href="/ii"> II </a> <br> <br> What do you call fish with no eyes? <br> FSH! <br> <img src ="https://s3.amazonaws.com/lodcf/wp-content/uploads/2014/06/09140445/nemojpg-3cafb3fbeb69a667.jpg" alt ="group photo">'

@app.route("/ii") #assign function to route
def pt2():
    return '<a href="/"> HOME </a> <a href="/i"> I </a> <br> <br> What do you call the security guards outside of Samsung? <br> GUARDIANS OF THE GALAXY <br> <img src ="https://cdn.vox-cdn.com/thumbor/xddVMltvqjB3PEgF4OnOQifZvZs=/0x0:1200x696/1200x800/filters:focal(535x82:727x274)/cdn.vox-cdn.com/uploads/chorus_image/image/58843699/baby-groot-guardians.0.0.jpg" alt ="group photo" height="400" width ="600">'

app.debug = True
app.run()

if __name__ == "__main__":
    app.debug = True;
    app.run()
