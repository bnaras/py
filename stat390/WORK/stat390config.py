################Configurable variables##################################
##
## Note for non-Unix users: All file names are best without spaces.
## Else you are expected to know how to escape spaces. HEED THIS!
##
## It is assumed admin, client and WORK are under this directory
## as it would be by default.
##
## Default suggestions are for Stanford
##

APP_DIR = 'Change to your dept cgi-bin directory' ## Change if you copy
APP_WEBROOT = 'https://web.stanford.edu/dept/<your_dept cgi-bin-directory>' ## Note URL!
APP_LOGGING = True  ## Allowable values True/False
LOG_DIR = APP_DIR + '/LOG' ## If logging is true above, ensure this exists
SMTP_SERVER = 'your smtp server' ## e.g. smtp.stanford.edu
CONSULTANTS_CSV = APP_DIR + "/WORK/consultants/test-consultants.csv" # change appropriately
STAT390_GROUP_FILE = APP_DIR + "/admin/.stat390group"

##
## The time slots, one per line. These should be the display value in the strict format
## specified in the example slots file. The corresponding blackout_time is computed
## automatically i.e. slots[i] will not be shown as a choice if the current time is
## beyond 6pm of the day of the time slot.
## Note: code to find blackout time is not great, don't push it. Or improve it.
##
TIME_SLOTS_FILE = APP_DIR + "/WORK/time-slots.txt"
## Advanced configuration possible in stat390common.py

