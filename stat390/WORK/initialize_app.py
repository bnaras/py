#!/usr/bin/env python

import sys
sys.path.append("../WORK")

from stat390common import *

## Save away previous database if it exists.
dbFileName = DB_URL[10:] ## drop the sqlite:/// prefix

if os.path.exists(dbFileName):
    backupFileName = dbFileName+ "-" + datetime.now().strftime("%Y-%m-%d:%H:%M:%S") + ".bak"
    os.rename(dbFileName, backupFileName)
    print "%(orig)s backed up as %(backup)s\n" % {"orig" : dbFileName, "backup" : backupFileName}

## create tables
Base.metadata.create_all(engine)

## populate timeslots in table.
## Sometimes people ask for 18:00 hours on same day as the blackout time
## that is easily accomplished with makeDateTime(slot, useEndTime=True).replace(hour=18)
timeslotValues = readSlotsFromFile(TIME_SLOTS_FILE)
timeSlots = [Timeslot(makeDateTime(slot), makeDisplayValue(slot), makeDateTime(slot, useEndTime=True)) for slot in timeslotValues]

# Now create all consultants from csv file
import csv
f = open(CONSULTANTS_CSV, "rU")
reader = csv.DictReader(filter(lambda line: not line.startswith('#'), f))
consultants = [Consultant(row['Sunet'].strip(' "'), row['Name'].strip(' "'), row['Role'].strip(' "')) for row in reader]

## create stat390 group file
with open(STAT390_GROUP_FILE, "w") as f:
    f.write("stat390:")
    for consultant in consultants:
        f.write(" " + consultant.sunet)
f.close()

# create a Session
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

