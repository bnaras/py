#!/usr/bin/env python
import sys
sys.path.append("../WORK")

from stat390common import *

indexHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>Stat 390 Consultants</title>
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/modern/reset.css" media="all" />
    <link rel="stylesheet" type="text/css" href="https://web.stanford.edu/dept/its/css/services/webforms/themes/stanford.css" media="all" />
    <link rel="stylesheet" type="text/css" href="table.css" />
</style>
</head>
  <body>

  <h1>Stat 390 Consultants</h1>

  <p>
  <table class="table">
  <tr>
    <th>Name</th>
    <th>Email</th>
  </tr>
  %(rows)s
  </table>
  </p>
    </body>
</html>
"""

tableRowHTML = """
<tr>
  <td>%(name)s</td>
  <td><a href="mailto:%(email)s">%(email)s</a></td>
<tr>
"""

session = sessionmaker(bind=engine)()

tableRowsHTML = ""
for consultant in session.query(Consultant):
    tableRowsHTML += tableRowHTML % {"name" : consultant.name,
                                     "email" : consultant.id}
session.close();
## Now just print the output
print 'Content-Type: text/html'
print # HTTP says you have to have a blank line between headers and content
print indexHTML % {"rows": tableRowsHTML}
