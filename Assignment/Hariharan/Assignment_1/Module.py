from flask import Flask
#Modules
from pyjokes import get_joke
from art import text2art
from webbrowser import open_new
from math import sqrt
from  datetime import datetime

app=Flask(__name__)
@app.route('/')
def home():
    return "Hi this is a home page go to opr/ for operations"
@app.route('/opr/Jokes/')
def Jokes():
    #Tells a programming Jokes whenever it reloads
    joke=get_joke(language='en',category='neutral')
    return joke
@app.route('/opr/Art/')
def Art():
    #Gives the Value in an art form
    txt=text2art('E')
    return txt
@app.route('/opr/Web/')
def web():
    #Opens the Website in the new Window of the default browser
    return open_new("https://www.w3schools.com/css/default.asp")
@app.route('/opr/Time/')
def Time():
    #Gives the Current Time and Date
     now = datetime.now()
     date_time = now.strftime("Date :%d/%m/%Y \n , Time :%H:%M:%S")
     return date_time
@app.route('/opr/Math/')
def Math():
    #Gives the Sqrt of the the Value
    return "The Square Root of 13 is %f" %sqrt(13)

if __name__=="__main__":
   app.run()