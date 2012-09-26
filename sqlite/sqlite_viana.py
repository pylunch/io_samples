# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# SQLite I/O
# ----------
# 
# The website for SQLite (including syntax) is: http://www.sqlite.org/  
#   
# First let's start by importing the sqlite3 python module.

# <codecell>

import sqlite3

# <markdowncell>

# Now let's creat a connection to a database. If the database does not exist it will be created. Next we create a `cursor` object that we'll use to interact with the database.

# <codecell>

connection = sqlite3.connect('test_database.db')
cursor = connection.cursor()

# <markdowncell>

# For performance keep in mind that creating connections is computationally expensive while cursor objects are cheap. The next step is to define our table structure. 

# <codecell>

cursor.execute('CREATE TABLE IF NOT EXISTS planets (name TEXT, moons INTEGER);')

# <markdowncell>

# Like all commands this one is executed with the `execute` method of the the `cursor` object. Let's look at what this command does. If there is not already a table in our database called planets it creates one. This table will have 2 columns (or "fields"), a text column called planets and an integer column called moons. Now let's examine the contents of our table.

# <codecell>

cursor.execute('SELECT * FROM planets;')
cursor.fetchall()

# <markdowncell>

# Again, we are using the `execute` method but this time because we want to see the output of our command (if there is any) we follow it with a call to the `fetchall` method. In this case we get a empty list back. This is exactly what we expect because we haven't put anything into that database yet. So let's add some data.

# <codecell>

cursor.execute('INSERT INTO planets (name, moons) Values ("Jupiter", "67");')
cursor.execute('INSERT INTO planets (name, moons) Values ("Neptune", "12");')
cursor.execute('INSERT INTO planets (name, moons) Values ("Saturn", "61");')

# <markdowncell>

# Now let's take another look and see what we have.

# <codecell>

cursor.execute('SELECT * FROM planets;')
cursor.fetchall()

# <markdowncell>

# Great! Except I made a mistake. Saturn doesn't have 61 moons, it has 62. Let's INSERT that data again and see if that fixes the problem.

# <codecell>

cursor.execute('INSERT INTO planets (name, moons) Values ("Saturn", "62");')
cursor.execute('SELECT * FROM planets;')
cursor.fetchall()

# <markdowncell>

# Whoops! Now we have 2 entries for Saturn. That's because there is no uniqueness contraint on either column, meaning we can have duplicates. We can also modify the SELECT statement to only return the records for Saturn.

# <codecell>

cursor.execute('SELECT * FROM planets WHERE name = "Saturn";')
cursor.fetchall()

# <markdowncell>

# Pretty straight-forward. Now let's use the DELETE command to remove that incorrect record for Saturn.

# <codecell>

cursor.execute('DELETE FROM planets WHERE moons == 61;')
cursor.execute('SELECT * FROM planets;')
cursor.fetchall()

# <markdowncell>

# Notice we used the value of 61 for the moons column to specify exactly which record should be deleted. So now we fixed that but I just noticed another mistake. Neptune has 13 moons not 12. So this time instead of adding a new record and removing the old one let's just update the existing record with the update command. 

# <codecell>

cursor.execute('UPDATE planets SET moons = 13 WHERE name = "Neptune";')
cursor.execute('SELECT * FROM planets;')
cursor.fetchall()

# <markdowncell>

# Great! Now things look right. Let's commit our changes (like hitting save) and close out our connection. 

# <codecell>

connection.commit()
connection.close()

# <markdowncell>

# We've just learned the basic SQLite commands of CREATE TABLE, SELECT, INSERT, DELETE, and UPDATE. We also learned how to use the Python SQLite3 module to interface with a SQLite database and execute those commands. From here you could easily expand this to fit your own projects. For example:
# 
#   * All the header information in your dataset.
#   * A log of when you ran your pipeline and what data you used.
#   * A daily snap shot of dataset as it accumulates new data.
# 
# As you start building more and more complex database interfaces you might find that would want to move to a more robust database toolkit such as SQLAlchemy: http://www.sqlalchemy.org/ 

# <codecell>


