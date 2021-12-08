# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 00:11:41 2021

@author: ranrakes
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute('use mydatabase')

def insert_user():
    sql = 'insert into student(roll_no,name,DOB,contact) values ( %s,%s,%s,%s)'
    vals = [
            ( 1, "User1","2021-10-10","8792684640"),
            ( 2, "User2","2021-1-10","1234567898"),
            ( 3, "User3","2021-11-10","987456578"),
            ( 4, "User4","2021-2-2","3434567876"),
            ( 5, "User5","2021-3-11","6767898765"),
            ( 6, "User6","2021-9-9","8987654323")
            ]    
    mycursor.executemany(sql, vals)
    mydb.commit()

    print(mycursor.rowcount," affected")
    
def do_setup():
    mycursor.execute("show tables")
    for x in mycursor:
        print(x[0])
        if x[0] == "student":
            return
    mycursor.execute('create table student ( roll_no INT PRIMARY KEY, name VARCHAR(255), DOB DATE, contact VARCHAR(20))')
    insert_user()


def save_student(data):
    sql = 'insert into student(roll_no,name,DOB,contact) values ( %s,%s,%s,%s)'
    val = ( data['roll_no'],data['name'],data['DOB'],data['contact'])    
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount," affected")

def get_student(data):
    sql = "SELECT * FROM student WHERE roll_no = %s"
    roll = (data, )
    mycursor.execute(sql, roll)    
    myresult = mycursor.fetchall()

    print(mycursor.rowcount," affected")
    if(mycursor.rowcount == 0):
        return "record not found check id"
    return myresult

def get_all_students():
    sql = "SELECT * FROM student"
    mycursor.execute(sql)    
    myresult = mycursor.fetchall()

    print(mycursor.rowcount," affected")    
    return myresult
    
def delete_student(id):
    sql = "DELETE FROM student WHERE roll_no = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    if(mycursor.rowcount == 0):
        return "record not found check id"
    return "Rows affected 1"


def update_student(id,data):
    sql = "Update student set name= %s,DOB=%s,contact=%s where roll_no = %s "
    val = (data['name'],data['DOB'],data['contact'],id)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    if(mycursor.rowcount == 0):
        return "record not found check id"
    return "Updated row count {}".format(mycursor.rowcount)
    
    