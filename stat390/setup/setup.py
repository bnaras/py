#!/usr/bin/env python

successHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat390 Consulting Website</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>
    <h1>Success</h1>
    <p> The setup was successful. Please try to create a random request and see if an email comes to you. Then you can return the database to its pristine
    state by setting it up once again using the same data.</p>
  </body>
</html>
"""

failureHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat390 Consulting Website</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
  </head>
  <body>
    <h1>Unsuccessful</h1>
    <p> The setup was <em>not successful</em>, error message below. Please fix and iterate.</p>
    <pre>
    %(msg)s
    </pre>
  </body>
</html>
"""

import sys
sys.path.append("../WORK")

from stat390common import *

feedbackHTML = ""

form = cgi.FieldStorage()
pFile = form['pFile']
tsFile = form['tsFile']

try:
    ## Ensure files got uploaded
    if (not pFile.file):
        raise Exception('Partcipant file not uploaded')
    if (not tsFile.file):
        raise Exception('Timeslot file not uploaded')
    
    ## Save away previous database if it exists.

    dbFileName = DB_URL[10:] ## drop the sqlite:/// prefix
    if os.path.exists(dbFileName):
        backupFileName = dbFileName+ "-" + datetime.now().strftime("%Y-%m-%d:%H:%M:%S") + ".bak"
        os.rename(dbFileName, backupFileName)
        print "%(orig)s backed up as %(backup)s\n" % {"orig" : dbFileName, "backup" : backupFileName}

    ## create tables
    Base.metadata.create_all(engine)

    ## populate timeslots in table.
    ## Sometimes people ask for 18:00 hours on same day as the blackout time (3rd arg to Timeslot).
    ## That is easily accomplished with makeDateTime(slot, useEndTime=True).replace(hour=18)
    timeslotValues = filter(lambda x: len(x) > 0 and not x.startswith('#'), [x.strip('\n\t\r') for x in tsFile.file.readlines()])
    timeSlots = [Timeslot(makeDateTime(slot), makeDisplayValue(slot), makeDateTime(slot, useEndTime=True)) for slot in timeslotValues]

    ## Now create all consultants from csv file
    import csv
    reader = csv.DictReader(filter(lambda line: not line.startswith('#'), pFile.file))
    consultants = [Consultant(row['Sunet'].strip(' "'), row['Name'].strip(' "'), row['Role'].strip(' "')) for row in reader]

    ## create stat390 group file
    with open(STAT390_GROUP_FILE, "w") as f:
        f.write("stat390:")
        for consultant in consultants:
            f.write(" " + consultant.sunet)
    f.close()

    ## create a Session
    session = sessionmaker(bind=engine)()
    session.add_all(consultants)
    session.add_all(timeSlots)
    session.commit()
    session.close()

    ## create proper stat390 admin .htaccess file
    with open(ADMIN_HTACCESS_FILE, "w") as f:
        f.write("AuthType WebAuth\n")
        f.write("AuthGroupFile " + STAT390_GROUP_FILE + "\n")
        f.write("require group stat390\n")
    f.close()
    feedbackHTML = successHTML
except Exception, e:
    feedbackHTML = failureHTML % {"msg" : str(e)}

print 'Content-Type: text/html'
print # HTTP says you have to have a blank line between headers and content
print feedbackHTML
