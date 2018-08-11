#--------------------------------------------------------------------------#
#					README!!!


# This is a project mainly for working out features for later projects, 
# Along the lines of security, and systems working behind a web page.

# The only security so far is a password hasher. It works by taking the 
# text inputted into the text bar, using request.form[''], storing it into 
# a variable and pushing it through the md5 hashing algorithm, then outputting
# it in the console. 

# in the future, it will be stored in an apache database, but at the moment 
# I am on a 11 hour flight, and have no way of setting up a couchdb database. 
# I will update this readme when I have it set up.
#--------------------------------------------------------------------------#

#					Issues:

# so far the only issues with this project are because of my knowledge on the
# Flask framework and python. I will work them out when I get to my home comp
# uter. One of the problems is with my show_information_test function. 
# I am getting an error ( Error method not allowed ) and I need to do further
# research on this error. I will come back later.

#---------------------------------------------------------------------------#

# the flash framework is not working, no errors, just not doing what it is 
# supposed to be doing, I will work it out later with reference to other 
# older projects.

#----------------------------------------------------------------------------#

# Reminder: I need to do research on password salting. I only have a hash fun
# ction and I am looking forward to increasing security with a salting func
# tion. I will post a hashing and salting project to github when I have 
# figured it out. 

# I also need to work on the character limitation function. Not working the way
# I want it to. Doesn't cause any errors just a paperweight at the moment.
# Remind me to work on that. 

# I also need to do some research json. For now I am just using a dictionary t
# o store my data, and it works pretty good, I just want it to be organized.
# either couchdb, mlab or json. 

#END------------------------------------------------------------------------>
