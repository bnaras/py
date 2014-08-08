#!/usr/bin/env python
import sys
sys.path.append("../WORK")

from stat390common import *

# the form
formHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Add a Consultant to Stat390</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>
  <h1>Add a Consultant to Stat 390</h1>
  <p>
    <div id="container">
    <form method="post" enctype="multipart/form-data" action="%(actionURL)s">
    <p><strong><abbr class="required" title="Required Field">*</abbr> indicates required fields.</strong></p>
    <p class="input_text ">

    <label>Name (Last, First)<abbr class="required" title="Required Field">*</abbr></label>
    <br />
    <input type="text" id="field_200881" class="input_text" name="name" value="" />
    </p>

    <p class="email ">

    <label>Email <abbr class="required"
    title="Required Field">*</abbr> (Please ensure this is correct!)</label>
    <br />
    <input type="email" id="field_200887" class="email" name="email" value="" />
    </p>

    <p class="action">
	  <button class="submit" type="submit">Add Consultant</button>
	</p>

    </form>
    </div>
  </p>
  </body>
</html>
"""

# the response
responseHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat 390 Consultant added</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>

  <h1>Stat 390 Consultant</h1>

  <p>
      %(name)s [ %(email)s ] has%(already)s been added as a consultant to
  Stat390 and a notification email sent.
  </p>
    </body>
</html>
"""

# the redirect, in case of incomplete form
redirectHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="refresh" content="0;url=%(formURL)s" />
    <title>Empty Form: You are going to be redirected</title>'
  </head>
  <body>
    <h1>Empty Form</h1>
    Redirecting... <a href="%(formURL)s">Click here if you are not redirected</a>
  </body>
</html>
"""

emailText = """
Name: %(name)s [ %(email)s ] has%(already)s been added as a consultant to Stat390.
"""
form = cgi.FieldStorage()
name = form.getfirst("name", "").strip()
email = form.getfirst("email", "").strip()

print 'Content-Type: text/html'
print # HTTP says you have to have a blank line between headers and content

if name == "" or email == "":
    print formHTML % {"actionURL" : ADD_CONSULTANT_URL}
else:
    # create a Session
    session = sessionmaker(bind=engine)()
    already = ""
    if session.query(Consultant).filter(Consultant.id == email).count() > 0: # already there
        already = " already"
    else: # add consultant
        consultant = Consultant(email, name)
        session.add(consultant)
        session.commit()
        ## Send email to Instructor and consultant
        emailStatus = send_email(INSTRUCTOR_EMAIL, "Stat390 Consultant%s Added" % already,
                                 emailText % {"name" : name, "email": email, "already": already})
        emailStatus = send_email(email, "Stat390 Consultant%s Added" % already,
                                 emailText % {"name" : name, "email": email, "already": already})
        
    ## close session
    session.close()        
    ## Fix response
    responseHTML = responseHTML % {"name" : name, "email": email, "already": already}
    ## Now just print out details for the requester
    print responseHTML
