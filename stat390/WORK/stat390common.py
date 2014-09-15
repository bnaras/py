from stat390config import *
##
## NOTHING BELOW WILL NEED TO BE TYPICALLY CHANGED UNLESS YOU KNOW WHAT
## YOU ARE DOING
##
# Request form html
requestFormHTMLPrologue = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>STAT 390 Consulting Request</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
    </script>
  </head>
  <body>
    <div id="container">

      <form method="post" enctype="multipart/form-data" action="%(actionURL)s">

	<h1>STAT 390 Consulting Request Form</h1>
	<p>Please fill in details regarding your consulting request and click
	  the submit button. You will get a confirmation of this request in your
	  email.</p>

	<p><strong><abbr class="required" title="Required Field">*</abbr> indicates required fields.</strong></p>
	<p class="input_text ">

	  <label>Name <abbr class="required" title="Required Field">*</abbr></label>
	  <br />
	  <input type="text" class="input_text" name="name" value="%(name)s" />
	</p>

	<p class="input_text ">

	  <label>Affiliation <abbr class="required" title="Required Field">*</abbr></label>
	  <br />
	  <input type="text" class="input_text" name="affiliation" value="" />
	</p>

	<p class="email ">

	  <label>Email <abbr class="required"
						title="Required Field">*</abbr> (Please ensure this is correct!)</label>
	  <br />
	  <input type="email" class="email" name="email" value="%(email)s" />
	</p>

	<p class="textarea ">

	  <label>Problem Description (10K word limit)<abbr class="required" title="Required Field">*</abbr></label>
	  <br />
	  <textarea class="textarea" name="description"
	  rows="20" cols="80" maxlength="10240"></textarea>
	</p>

	<p class="textarea ">
	  <label>Web Links </label>
	  <br />
	  <textarea class="textarea" name="webLinks" rows="3" cols="80"></textarea>
	</p>

	<p class=" ">
	  <label>When do you plan to visit the consulting service?</label>
	  <br />
	  <select class="" name="visitTime">
"""
requestFormHTMLEpilogue = """
	  </select>
	</p>

	<p class="action">
	  <button class="submit" type="submit">Submit Request</button>
	</p>
      </form>
    </div>
  </body>
</html>
"""

## details of a specific request identified by id in HTML
reqIndexHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Request Id: %(id)s </title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>

  <h1>Request %(id)s</h1>

  <h3>%(name)s [ %(affiliation)s ]</h3>

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

      <form method="post" enctype="multipart/form-data" action="%(actionURL)s">
	<p class="textarea ">
	  <label>Enter Report</label>
	  <br />
      (Note: Include your name(s) on a separate line at the beginning)<br/>
	  <textarea class="textarea" name="report"
	  rows="20" cols="80" maxlength="10240">%(report)s</textarea>
	</p>

	<p class="action">
	  <button class="submit" type="submit">Submit Report</button>
	</p>
      </form>
    </body>
</html>
"""

reqDisplayHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Request Id: %(id)s </title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>

  <h1>Request %(id)s</h1>

  <h3>%(name)s [ %(affiliation)s ]</h3>

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

    <p>
	 <label>Report</label><br/>
     %(report)s
     </p>
    </body>
</html>
"""


noSuchRequestPage = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat 390 Request %(id)s</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
<body>No such request found. Check the request identifier %(id)s</body></html>
"""

################ End of Configurable variables##########################

WORK_DIR = APP_DIR + '/WORK'
REQUEST_FORM_URL = APP_WEBROOT + '/client/create_request.py'
DISPLAY_REQUESTS_URL = APP_WEBROOT + '/admin/display_requests.py'
ADD_CONSULTANT_URL = APP_WEBROOT + '/admin/add_consultant.py'
DB_URL = 'sqlite:///' + WORK_DIR + '/' + 'requests.sqlite3'

## Compute the blackout times for each quarter
from datetime import datetime
def makeDateTime(x):
    offset = 0
    terms = x.split()
    if (len(terms) != 4):
        raise Exception('Bad time slot format: ' + x)
    mon = terms[0]
    day = terms[1].split(',')[0]
    if (len(day) == 1):
        day = '0' + day
    endTime = terms[2].split("-")[1]
    if (terms[3].find('pm') >= 0):
        offset = 12
    dateStr = mon + ' ' + day + ' ' + str(datetime.now().year) + ' ' + str(int(endTime) + offset) + ':00:00'
    return datetime.strptime(dateStr, "%b %d %Y %H:%M:%S")

BLACKOUT_TIMES = [ makeDateTime(x) for x in AVAILABLE_DATES ]

import cgi, cgitb, fcntl, os, smtplib
##
## Function to generate the relevant available dates based on blackout_dates
##
def generateRequestFormHTML():
    result = requestFormHTMLPrologue
    current_time = datetime.now()
    for value in [AVAILABLE_DATES[x] for x in range(len(BLACKOUT_TIMES)) if BLACKOUT_TIMES[x] > current_time]:
        result += '<option value="' + value + '">' + value + '</option>\n'
    return result + requestFormHTMLEpilogue

## The next id is one more than the number of directories in the data dir
## prefixed by the letter C. The number is pre-padded with zeros to 3 digits.
def nextId(dataDir):
    return ("C" + format(len(os.listdir(dataDir)) + 1, "03d"))

## Return a list of all current ids in reverse chronological order
##
def revChronId(dataDir):
    n = len(os.listdir(dataDir))
    return (["C" + format(x, "03d") for x in range(n, 0, -1) ])

#send_email function: sends message from from_addr, assumes valid input
def send_email(to_addr, subject, message):
  #form the email headers/text:
  from_addr = "Stat 390 Do Not Reply <nobody@stanford.edu>"
  email_body =  "From: " + from_addr + "\n"
  email_body += "To: " + to_addr + "\n"
  email_body += "Subject: %s\n" % subject
  email_body += "\n"
  email_body += message
  #return true for success, false for failure:
  try:
    server = smtplib.SMTP(SMTP_SERVER)
    server.sendmail(from_addr, to_addr, email_body)
    server.quit()
    return True;
  except smtplib.SMTPException:
    return False;
  #end of send_email function

########################################################################

from sqlalchemy import create_engine, ForeignKey, func
from sqlalchemy import Column, DateTime, Integer, String, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine(DB_URL, echo=False)
Base = declarative_base()

########################################################################

########################################################################
class Consultant(Base):
    """"""
    __tablename__ = "consultant"
    id = Column(String(50), primary_key=True)
    name = Column(String(40))

    def __init__(self, email, name):
        """"""
        self.id = email
        self.name = name

    def __repr__(self):
        return "<Consultant(%(name)s [%(email)s])>" % {"name" : self.name, "email" : self.id}

class Request(Base):
    """"""
    __tablename__ = "request"
    id = Column(String(4), primary_key=True)
    name = Column(String(40))
    affiliation = Column(String(50))
    email = Column(String(50))
    emailSent = Column(Boolean)
    description = Column(String(10245))
    webLinks = Column(String(205))
    visitTime = Column(String(25))
    requestTime = Column(DateTime)
    consultant_id = Column(String(50), ForeignKey("consultant.id"))
    consultant = relationship("Consultant", backref=backref('request', order_by=id))
    report = Column(String(10245))

    def __init__(self, id, name, affiliation, email, emailSent, description, webLinks, visitTime, requestTime):
        """"""
        self.id = id
        self.name = name
        self.affiliation = affiliation
        self.email = email
        self.emailSent = emailSent
        self.description = description
        self.webLinks = webLinks
        self.visitTime = visitTime
        self.requestTime = requestTime

    def __repr__(self):
        return "<Request('%(id)s', '%(visitTime)s', '%(name)s [%(affiliation)s]')>" % {"id" : self.id, "visitTime" : self.visitTime, "name" : self.name, "affiliation" : self.affiliation}


########################################################################

if (APP_LOGGING):
    cgitb.enable(display=1, logdir=LOG_DIR)
