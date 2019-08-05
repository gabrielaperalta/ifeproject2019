import os
from app import app
from flask import render_template, request, redirect, session, url_for

app.secret_key = b'y\xd7;\xc4\xd5\xdf\x1a\xc2\xb4\x91=q\x95\xdf\xa8\xba'

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database' 
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:P0nmZdLUGmYS1a1I@cluster0-ymemu.mongodb.net/database?retryWrites=true&w=majority' 

mongo = PyMongo(app)



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
    
@app.route('/leviinfo')

def leviinfo():
    return render_template('leviinfo.html')
    
@app.route('/index2')

def index2():
    return render_template('index2.html')

@app.route('/login')

def login():
    return render_template('login.html')
    



#Log In:
@app.route('/login', methods=['POST'])
def loginasuser():
    users = mongo.db.users
    # use the username to find the account
    existing_user = users.find_one({"Email":request.form['Email']})
    if existing_user:
        # check if the password is right
        if existing_user['Password'] == request.form['Password'] :
            session['Email'] = request.form['Email']
            return redirect(url_for('index2'))
        else:
            return "Your password doesn't match your email."
    else:
        return "There is no email with that username. Try making an account."

#Log In:
@app.route('/login', methods=['POST'])
def loginasmember():
    users = mongo.db.users
    # use the username to find the account
    existing_user = users.find_one({"Email":request.form['Email']})
    if existing_user:
        # check if the password is right
        if existing_user['Password'] == request.form['Password'] :
            session['Email'] = request.form['Email']
            return redirect(url_for('index2'))
        else:
            return "Your password doesn't match your email."
    else:
        return "There is no email with that username. Try making an account."
  
# #   LOG OUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
  
# #   LOG OUT
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')
    
# SIGN-UP:

@app.route('/signup', methods = ['POST', 'GET'])
def usersignup():
    if request.method =="POST":
        users = mongo.db.users
        # users.insert({"Email":request.form['Email'],"Password":request.form['Password']})
        # db.session.add(data)
        # db.session.commit()
        existing_user = users.find_one({"Email":request.form["Email"]})
        if existing_user is None:
            users.insert({"Email":request.form['Email'],"Password":request.form['Password']})
            return render_template('shop.html')
        else:
            return "That email is taken. Try logging in, or try a different email"
    else:
        return render_template('signup.html')

@app.route('/signupmember', methods = ['POST', 'GET'])
def membersignup():
    if request.method =="POST":
        members = mongo.db.members
        # users.insert({"Email":request.form['Email'],"Password":request.form['Password']})
        # db.session.add(data)
        # db.session.commit()
        existing_member = members.find_one({"Email":request.form["Email"]})
        if existing_member is None:
            members.insert({"Email":request.form['Email'],"Password":request.form['Password']})
            return render_template("add_clothes.html")
        else:
            return "That email is taken. Try logging in, or try a different email"
    else:
        return render_template('signupmember.html')
        
@app.route('/checkout')
def  checkout():
    return render_template('checkout.html')
    
@app.route('/pay')
def pay():
    return render_template('pay.html')
@app.route('/addclothes')
def add_clothes():
    return render_template('add_clothes.html')
    
@app.route('/cart')
def cart():
    return render_template('cart.html')
    
@app.route('/yourstore')
def yourstore():
    return render_template('yourstore.html')
# CONNECT TO DB, ADD DATA

# @app.route('/add')

# def add():
#     # connect to the database

#     # insert new data

    # return a message to the user
    
