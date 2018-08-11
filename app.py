from flask import Flask, redirect, url_for, session, request, Markup, render_template, flash
import hashlib
import couchdb

app = Flask(__name__) #app data

app.secret_key = 'dog' #secret key

couch = couchdb.Server() #stores server data 127.0.0.1:59874/_utils/index.html/form-project/_all_docs
db = couch['form-project'] #existing database

@app.route('/')
def render_home():
    return render_template('index.html') #render the home page

#function for creating accounts
@app.route('/createaccnt' , methods=['POST'])
def create_accnt():
    fname = request.form['fname']  #create variables for all fields of form; set equal to values
    lname = request.form['lname']
    usr_email = request.form['email']
    user_name = request.form['uname']
    user_password = request.form['password']
    data_doc = {                        #new document
        'firstname' : fname,
        'lastname': lname,
        'email': usr_email,
        'username': user_name,
    }
    db.save(data_doc)
    hash_password(user_password,data_doc) #call hashing function
    charLengthLim(usr_email,user_name,fname,lname,user_password) #call input length function
    if len(usr_email) & len(user_password) & len(user_name) & len(fname) & len(lname) > 0:
        print("render the display html file")
        render_display() #if the lengths of any of the values is greater than 0, the page display.html is rendered
    elif len(usr_email) | len(user_password) | len(user_name) | len(fname) | len(lname) == 0:
        print("You did not fill in all of the fields")
        redirect_to_login() #otherwise, the login page is rendered again
    return render_display()

#function for hashing passwords  (just a security measure)
def hash_password(user_password,data_doc):
    hashed_password = hashlib.md5(user_password.encode()) #create hashed password variable by hashing the input for user_password form (md5 encryption)
    data_doc['password'] = hashed_password.hexdigest()
    print (hashed_password.hexdigest()) #print the hashed password !(read further documentation on hashlib)!
    return None                         #hexdigest converts the hash value into a string

#function for reporting short un, pw, and ue character lenghts
def charLengthLim(usr_email,user_name,fname,lname,user_password):    
    if len(usr_email) < 1:
        flash("Your Email is too Short")
    elif len(user_name) < 1:
        flash("Your User Name is too Short")  
    elif len(user_password) < 1:
        flash("Your Password is too Short")
    elif len(usr_email) > 50:
        flash("Your Email is too Long")
    elif len(user_name) > 50:
        flash("Your User Name is too Long")
    elif len(user_password) > 50:
        flash("Your Password is too Long")
    else:
        print("everything should be good")
        print(len(usr_email))
        print(len(user_name))
        print(len(user_password))
    return None

@app.route('/showinfo' , methods=['POST'])
def show_information_test(data_doc):
    info = ''
    info += '<h1> Firstname: ' + data_doc['firstname'] + '</h1>'
    info += '<h1> Lastname: ' + data_doc['lastname'] + '</h1>'
    info += '<h1> Email: ' + data_doc['email'] + '</h1>'
    info += '<h1> User Name: ' + data_doc['username'] + '</h1>'
    info += '<h1> Password: ' + data_doc['password'] + '</h1>'
    return Markup(info)

def document_data_present(data_doc, fname, lname, user_name, usr_name, user_password):
    if fname | lname | user_name | usr_name | user_password in data_doc:
        flash('already in database')
    return None

@app.route('/redir')
def redirect_to_login():
    return render_template('createacct.html')

@app.route('/display')
def render_display():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)


# REMEMBER LAST ERROR WAS METHOD NOT ALLOWED ON SHOWINFO FUNCTION
