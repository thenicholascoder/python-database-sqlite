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
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# get a file name
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

# loop through it
for line in fh:

    # we need only From lines
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    # database starts here
    # dictionary part
    # select count from database
    # ? = placeholder, replaced by tuple email
    # this is not retrieving a data
    # cur.execute = opening a set of records that are going to read file
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))

    # grab the first one, and give it back in row
    # row = info from database
    row = cur.fetchone()

    # if it is not seen on the rows on the table
    if row is None:

        # insert into Counts (email,count) VALUES(?,1), ? = placeholder (email,) as parameter
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))

    # if the row exists
    else:

        # we will just add 1 to the value of the key where email is the placeholder, (email,) = tuple
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))

    # it will write to disk, you can commit ever 10 or 100
    # if its online you can commit every screen thing
    conn.commit()

# WE WILL RUN THE DATABASE, DESC LIMIT  = TOP 10
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'


# executing cur.execute(sqlstr), for each of it
for row in cur.execute(sqlstr):

    # this will print a tuple where row0 = email, row1 = count
    print(str(row[0]), row[1])

# then we will close the connection
cur.close()
