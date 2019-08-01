import os
from app import app
from flask import render_template, request, redirect

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]


# from flask_pymongo import PyMongo

# name of database
# app.config['MONGO_DBNAME'] = 'database-name' 

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri' 

# mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')

@app.route('/shop')
 
def shop():
    return render_template('shop.html')
    

@app.route('/signup')

def signup():
    return render_template('signup.html')
    
# SIGN-UP:

@app.route('/signup', methods = ['POST', 'GET'])
def usersignup():
    return redirect("shop.html")


# CONNECT TO DB, ADD DATA

# @app.route('/add')

# def add():
#     # connect to the database

#     # insert new data

    # return a message to the user
    
