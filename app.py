from flask import Flask, redirect, url_for, session, request, jsonify, Markup, make_response, render_template, flash
import os
import json
import hashlib

#--------------------#

app = Flask(__name__)

#----------Secret--Key-------------#

app.secret_key = 'dog'

#--------Global--Variables---------#


#--------------------#

@app.route('/')
def render_home():
    return render_template('index.html')

#-------------------------------------------------------------------------------------------------------------------------#

#function for creating accounts
@app.route('/createaccnt' , methods=['POST'])
def create_accnt():
    fname = request.form['fname']  #create variables for all fields of form; set equal to values
    lname = request.form['lname']
    usr_email = request.form['email']
    user_name = request.form['uname']
    user_password = request.form['password']
    json_data = {}
    json_data['firstname'] = fname
    json_data['lastname'] = lname
    json_data['email'] = usr_email
    json_data['username'] = user_name
    hash_password(json_data,user_password) #call hashing function
    charLengthLim(usr_email,user_name,fname,lname,user_password) #call input length function
    print(json_data) #print data
    if len(usr_email) & len(user_password) & len(user_name) & len(fname) & len(lname) > 0:
        print("render the display html file")
        render_display() #if the lengths of any of the values is greater than 0, the page display.html is rendered
    elif len(usr_email) | len(user_password) | len(user_name) | len(fname) | len(lname) == 0:
        print("You did not fill in all of the fields")
        redirect_to_login() #otherwise, the login page is rendered again
    return render_display()
#---------------------------------------------------------------------------------------------------------------------------#

#function for hashing passwords  (just a security measure)
def hash_password(json_data,user_password):
    hashed_password = hashlib.md5(user_password.encode()) #create hashed password variable by hashing the input for user_password form (md5 encryption)
    json_data['Password'] = hashed_password # add hashed password to json file to be stored
    print (hashed_password.hexdigest()) #print the hashed password !(read further documentation on hashlib)!
    return None                         #hexdigest converts the hash value into a string

#---------------------------------------------------------------------------------------------------------------------------#

#function for reporting short un, pw, and ue character lenghts
def charLengthLim(usr_email,user_name,fname,lname,user_password):    
    if usr_email < 1:
        flash("Your Email is too Short")
    elif user_name < 1:                                                    
        flash("Your User Name is too Short")  
    elif user_password < 1:
        flash("Your Password is too Short")
    elif usr_email > 50:
        flash("Your Email is too Long")
    elif user_name > 50:
        flash("Your User Name is too Long")
    elif user_password > 50:
        flash("Your Password is too Long")
    else:
        print("yo b everything good in the hood")
        print(usr_email)
        print(user_name)
        print(user_password)
    return None

#----------------------------------------------------------------------------------------------------------------------------#

@app.route('/showinfo' , methods=['POST'])
def show_information_test(usr_email,user_name,fname,lname,user_password):
    info = ''
    info += '<h1> Firstname: ' + str(fname) + '</h1>'
    info += '<h1> Lastname: ' + str(lname) + '</h1>'
    info += '<h1> Email: ' + str(usr_email) + '</h1>'
    info += '<h1> User Name: ' + str(user_name) + '</h1>'
    info += '<h1> Password: ' + str(user_password) + '</h1>'
    return Markup(info)

#------------------------------------------------------------------------------------------------------------------------------#

@app.route('/redir')
def redirect_to_login():
    return render_template('createacct.html')

#------------------------------------------------------------------------------------------------------------------------------#

@app.route('/display')
def render_display():
    return render_template('display.html')

#------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True,port=5000)


# REMEMBER LAST ERROR WAS METHOD NOT ALLOWED ON SHOWINFO FUNCTION