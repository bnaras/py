# A Simple webapp for Consulting Requests (like Stat390)

This is a simple webapp with a python form handler backed by a SQLite
database for managing consulting requests. The available paths for the
webapp are:

1. `/client/create_request.py` for making consulting requests.

2. `/admin/index.html` for students and instructors participanting in
   the class.

3. `/setup/index.html` for staff to set up the application at the
   beginning of each quarter. 

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
(the `sys.path.append` part). But not recommended unless you really
understand the code. So you should generally leave the directory
structure exactly as included: `admin`, `client` and `WORK` at the
same level!

## At the start of a new quarter

### Web interface setup

Follow these instructions to set up the class site using a web form. 

1. Prepare a CSV file containing the name of the instructor. As a test, you should first add yourself as an instructor . The format of the file is as follows:

  1. Any line starting with `#` is a comment and will be ignored.
  2. The first non-comment line encountered should be a header line exactly as follows (with quotes): 
```
"Name","Sunet","Role"
```
  3. Lines should contain three columns: `full_name`, `sunet`, `role`, each quoted. Note that we need the `sunet` id, which may not be the stanford email id. The allowable roles are student or instructor (case matters). 
```
"Blow, Joe","foobar","instructor"
```
2. Prepare a text file of time slots when the class will meet. Here is an example.
```
##
## Any line starting with # is a comment and will be ignored.
## Thus it is easy to drop slots by just commenting it out.
##
## ONLY allowed formats (spaces, commas important): 
##  "Jan 10, 10:00-12:00" or "Feb 2, 12:00-14:00" or "Mar 2, 9:00-11:00"
##  "Apr 10, 11:30-13:30"
##
Dec 25, 8:00-10:00
Dec 25, 11:00-13:00
Dec 25, 15:00-16:00
Dec 26, 9:00-10:00
Dec 26, 11:00-14:00
```
3. Access the `setup` page in your browser and upload these two files as noted on the form. The `setup` page URL is typically:
```
https://<your_web_root_URL>/cgi-bin/stat390/setup/
```
4. Once set up, try out a form request by accessing
```
https://<your_web_root_URL>/cgi-bin/stat390/client/create_request.py
```
   and filling out the form.  Make a few testing requests.

5. Access the admin interface and see the reports at
```
https://<your_web_root_URL>/cgi-bin/stat390/admin/
```
   Access one of the requests and add to the report field and save.
   If all goes well, then you can repeat step 3 with the actual list
   of class instructor/students and timeslots.

### Command-line interface

The format of the data is exactly the same as in the web
interface. You have to create the files as specified there. 

1. Edit `WORK/stat390config.py` appropriately, if not already done
   so. The defaults are already set for the Department of Statistics,
   so about the only thing that might need to be modified is the name
   of the initial consultants file and the time-slots file. Some basic
   examples are provided with the app. The year is assumed to be
   the current year.

2. Change directory to the `WORK` directory and run the script
   `initialize_app.py` to initialize the database
   (`./initialize_app.py` on any of the `corn` machines should usually
   do it).

Test it out as noted on the web form setup instructions.
