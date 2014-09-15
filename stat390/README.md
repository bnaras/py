# A Simple webapp for Consulting Requests (like Stat390)

This is a simple webapp with a python form handler backed by a SQLite
database for managing consulting requests.

The Stanford infrastructure requires that you enable cgi scripts in
your web space if you have not already done so; see the
[https://tools.stanford.edu/ Stanford Tools] web page for this.

The client directory contains the `.htaccess` and python form handler
for the consulting clients.  By default, it is set up so that Stanford
associated people can make requests.  Remains invariant over quarters
for Stanford folks.

The admin directory is for the class participants and the
instructor. There is a `.htaccess` file that controls access so that
only those in Stat390 class can access things. Changes by quarter.

Both directories contain python cgi scripts that need access to the
common code and database in the `WORK` directory.

Only the `admin` and the `client` directories need to be in `cgi-bin`
in the Stanford web infrastructure. The `WORK` directory _should not
be visible_ over the web. You can probably move it elsewhere and
change the code in the admin and client files to reflect its location
(the sys.path.append part). The current code assumes that the
directory structure is exactly as included: `admin`, `client` and
`WORK` are at the same level!

## At the start of a new quarter

* Edit `admin/.htaccess` and add only instructor sunet ID. For example,
  `require user naras` for just me.
* Edit `WORK/stat390config.py` appropriately. Make sure you set
   instructor email correctly. And update the available dates for the
   consulting sessions. The year is assumed to be the current year.
* `cd` to `WORK` directory and copy `requests.sqlite3-starter` to
   `requests.sqlite3`
* If you specified a csv file of students enrolled for the quarter,
   i.e. the student consultants in step 2, just run
   `initialize_consultants.py` to populate the database. You can add
   others via a web interface if people enroll later. For example, my
   consultant csv file just contains my full name and email address
   in addition to the header line.
* With every consultant added/deleted, add or remove their sunet id in
   `admin/.htaccess`.  YES, this has to be done manually even if you
   use the web interface to add consultants.
* Try out the form, by creating a request. The URL will be typically
   something like
   `https://<your_root>/cgi-bin/stat390/client/create_request.py` and
   make a request and ensure that everything works. After that you can
   replace the database in step 3 again with the starter database at
   which point the class is good to go.

