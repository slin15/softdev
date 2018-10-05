#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

print("STUDENTS")
with open('peeps.csv') as csvfile:
    #command = "CREATE TABLE roster (name TEXT, age INTEGER, userid INTEGER);"        #build SQL stmt, save as string
    #c.execute(command)    #run SQL statement 
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'], row['id'])
        #command = "INSERT INTO roster VALUES(row['name'])"
        #c.execute(command)
        

print("\n COURSES")
with open('courses.csv') as csvfile:
    #command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string
    #c.execute(command)    #run SQL statement
    reader = csv.DictReader(csvfile)
    for row in reader: 
        print(row['code'], row['mark'], row['id'])

#==========================================================


db.commit() #save changes
db.close()  #close database


