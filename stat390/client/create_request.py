#!/usr/bin/env python

import sys
sys.path.append("../WORK")

from stat390common import *
# the user sees what's below upon successful post
reqIndexHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>%(name)s [ %(affiliation)s ]</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>


  <h1>%(name)s [ %(affiliation)s ]</h1>

  <p>
  <label>Email</label><br/>
    <a href="mailto:%(email)s">%(email)s</a>
    </p>

    <p>
    <label>Description</label><br/>
    %(description)s
    </p>

    <p>
    <label>Web Links</label><br/>
    %(webLinks)s
    </p>

    <p>
    <label>Visit Time</label><br/>
    %(visitTime)s
    </p>

    <p>
    <label>Time of Request</label><br/>
    %(requestTime)s
    </p>

    <p>
    <label>Email confirmation sent successfully?</label><br/>
    %(emailStatus)s
    </p>

    </body>
</html>
"""

emailText = """
Stat 390 Consulting Request Details

Name: %(name)s [ %(affiliation)s ]

Description:
%(description)s

Web Links:
%(webLinks)s

Visit Time: %(visitTime)s

Time of Request: %(requestTime)s
"""

wName = os.environ['WEBAUTH_LDAP_DISPLAYNAME'];
wUser = os.environ['WEBAUTH_USER'];
wEmail = os.environ['WEBAUTH_LDAP_MAIL'];

form = cgi.FieldStorage()
affiliation = form.getfirst("affiliation", "").strip()
description = form.getfirst("description", "").strip()
webLinks = form.getfirst("webLinks", "")

print 'Content-Type: text/html'
print # HTTP says you have to have a blank line between headers and content

if affiliation == "" or description == "":
    print generateRequestFormHTML() % {"name" : wName, "email" : wEmail, "actionURL" : REQUEST_FORM_URL}
else:
    name = form.getfirst("name", "")
    email = form.getfirst("email", "")
    visitTime = form.getfirst("visitTime", "")
    requestTime = datetime.now()
    ## Send email
    emailStatus = send_email(email,
                             "Stat390 Consulting Request Submission",
                             emailText % {"name" : name,
                                          "affiliation" : affiliation,
                                          "description" : description,
                                          "visitTime" : visitTime,
                                          "webLinks" : webLinks,
                                          "requestTime" : requestTime.strftime("%Y-%m-%d %H:%M:%S")})
    ## Write index.html in a new subdirectory DATA_DIR/request_id
    indexHTMLContents = reqIndexHTML % {"name" : name,
                                        "email" : email,
                                        "affiliation" : affiliation,
                                        "description" : description,
                                        "visitTime" : visitTime,
                                        "webLinks" : webLinks,
                                        "requestTime" : requestTime.strftime("%Y-%m-%d %H:%M:%S"),
                                        "emailStatus" : emailStatus}

    # create a Session and update database
    session = sessionmaker(bind=engine)()
    id = "C" + format(session.query(Request).count() + 1, "03d") # the next id
    req_record = Request(id, name, affiliation, email, emailStatus, description, webLinks, visitTime, requestTime)
    session.add(req_record)
    session.commit()
    session.close()
    ## Now just print out details for the requester
    print indexHTMLContents

