#!/usr/bin/python
# datademo.py
# a simple script to pull some data from MySQL

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="dados")

# create a cursor for the select
cur = db.cursor()

# execute an sql query
cur.execute("SELECT name FROM dados.contatos")

# Iterate
for row in cur.fetchall():
      # data from rows
    name = str(row[0])

    # print
    print "This Person's name is " + name

# close the cursor
cur.close()

# close the connection
db.close()
