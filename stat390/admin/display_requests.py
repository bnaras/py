#!/usr/bin/env python

import sys
sys.path.append("../WORK")

from stat390common import *

indexHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat 390 Consulting Requests</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
    <link rel="stylesheet" type="text/css" href="table.css" />
</style>
</head>
  <body>
  
  <h1>Requests in Reverse Chronological Order</h1>

  <p>
  <table class="table">
  <tr>
    <th><a href="%(displayRequestURL)s">Request ID</a></th>
    <th>Request Date</th>
    <th><a href="%(displayRequestURL)s?sortBy=visitTime">Visit Time</a></th>
    <th>Name [Affiliation]</th>
  </tr>
  %(rows)s
  </table>
  </p>
    </body>
</html>
"""

tableRowHTML = """
<tr>
  <td><a href="%(url)s">%(id)s</a></td>
  <td>%(requestTime)s</td>
  <td>%(visitTime)s</td>
  <td>%(name)s [%(affiliation)s]</td>
<tr>
"""

form = cgi.FieldStorage()
id = form.getfirst("id", "").strip()
sortBy = form.getfirst("sortBy", "").strip()
report = form.getfirst("report")

print 'Content-Type: text/html'
print # HTTP says you have to have a blank line between headers and content

session = sessionmaker(bind=engine)()
slots = session.query(Timeslot)

if id == "":
    ## Read from the SQLITE database
    tableRowsHTML = ""
    if sortBy == "":
        for request in session.query(Request).order_by(Request.id.desc()):
            visitSlot = next(x for x in slots if x.startTime == request.visitTime) 
            tableRowsHTML += tableRowHTML % {"id" : request.id,
                                             "url" : DISPLAY_REQUESTS_URL + '?id='+ request.id,
                                             "requestTime" : request.requestTime.strftime("%Y-%m-%d %H:%M:%S"),
                                             "visitTime" : visitSlot.displayValue,
                                             "name" : request.name,
                                             "affiliation" : request.affiliation}
    else:
        for request in session.query(Request).order_by(Request.visitTime.desc()):
            visitSlot = next(x for x in slots if x.startTime == request.visitTime) 
            tableRowsHTML += tableRowHTML % {"id" : request.id,
                                             "url" : DISPLAY_REQUESTS_URL + '?id='+ request.id,
                                             "requestTime" : request.requestTime.strftime("%Y-%m-%d %H:%M:%S"),
                                             "visitTime" : visitSlot.displayValue,
                                             "name" : request.name,
                                             "affiliation" : request.affiliation}
        
    print indexHTML % {"rows": tableRowsHTML, "displayRequestURL" : APP_WEBROOT + '/admin/display_requests.py'}
else:
    request = session.query(Request).filter(Request.id==id).first()
    visitSlot = next(x for x in slots if x.startTime == request.visitTime)     
    if request is None:
        print noSuchRequestPage % {"id" : id}
    else:
        if report is not None: # Edited report was posted so save it.
            request.report = report
            session.commit()
            print reqDisplayHTML % {"id" : request.id,
                                    "name" : request.name,
                                    "email": request.email,
                                    "description" : request.description,
                                    "affiliation" : request.affiliation,
                                    "requestTime" : request.requestTime.strftime("%Y-%m-%d %H:%M:%S"),
                                    "webLinks" : request.webLinks,
                                    "visitTime" : visitSlot.displayValue,
                                    "emailStatus" : request.emailSent,
                                    "report" : request.report}
        else:
            reportText = request.report
            if reportText is None:
                reportText = ""
            actionURL = DISPLAY_REQUESTS_URL + '?id=' + request.id
            print reqIndexHTML % {"id" : request.id,
                                  "actionURL" : actionURL,
                                  "name" : request.name,
                                  "email": request.email,
                                  "description" : request.description,
                                  "affiliation" : request.affiliation,
                                  "requestTime" : request.requestTime.strftime("%Y-%m-%d %H:%M:%S"),
                                  "webLinks" : request.webLinks,
                                  "visitTime" : visitSlot.displayValue,
                                  "emailStatus" : request.emailSent,
                                  "report" : reportText}
                        
session.close()

