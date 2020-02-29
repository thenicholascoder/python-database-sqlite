# Your current grade on this assignment is: 100%

# To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:

# (Must have a .sqlite suffix)
# Hint: The top organizational count is 536.
# You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.


# import library of sqlite3
import sqlite3

# connects database to check access to the file
conn = sqlite3.connect('emaildb.sqlite')

# handle for sql, open -> send sql commands from cursor -> get response -> throw to handler
cur = conn.cursor()

# will drop table if there is any
cur.execute('DROP TABLE IF EXISTS Counts')

# create a table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# get a file name
fname = input('Enter file name: ')

# if there is len(fname)<1 then fname equals mbox.txt
if (len(fname) < 1): fname = 'mbox.txt'

# second file handler
fh = open(fname)

# loop through it
for line in fh:

    # we need only From lines
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    # dom
    findemail = email.find('@')

    # org
    org = email[findemail+1:len(email)]

    # database starts here
    # dictionary part
    # select count from database
    # ? = placeholder, replaced by tuple email
    # this is not retrieving a data
    # cur.execute = opening a set of records that are going to read file
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    # grab the first one, and give it back in row
    # row = info from database
    row = cur.fetchone()

    # if it is not seen on the rows on the table
    if row is None:

        # insert into Counts (email,count) VALUES(?,1), ? = placeholder (email,) as parameter
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))

    # if the row exists
    else:

        # we will just add 1 to the value of the key where email is the placeholder, (email,) = tuple
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# it will write to disk, you can commit ever 10 or 100
# if its online you can commit every screen thing
# outside the loop***********************************************
conn.commit()

# WE WILL RUN THE DATABASE, DESC LIMIT  = TOP 10
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'


# executing cur.execute(sqlstr), for each of it
for row in cur.execute(sqlstr):

    # this will print a tuple where row0 = email, row1 = count
    print(str(row[0]), row[1])

# then we will close the connection
cur.close()


# ***************************************************************
# OUTPUT
# iupui.edu 536
# umich.edu 491
# indiana.edu 178
# caret.cam.ac.uk 157
# vt.edu 110
# uct.ac.za 96
# media.berkeley.edu 56
# ufp.pt 28
# gmail.com 25
# et.gatech.edu 17

# Process finished with exit code 0
