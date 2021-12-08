import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute('use mydatabase')

def insert_contacts():
    sql = 'insert into contacts(name,contact) values (%s,%s)'
    vals = [
            ( "User1","8792684640"),
            ( "User2","1234567898"),
            ( "User3","987456578"),
            ( "User4","3434567876"),
            ( "User5","6767898765")
            ]    
    mycursor.executemany(sql, vals)
    mydb.commit()

    print(mycursor.rowcount," affected")
    
def do_setup():
    mycursor.execute("show tables")
    for x in mycursor:
        print(x[0])
        if x[0] == "contacts":
            return
    mycursor.execute('create table contacts ( id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), contact VARCHAR(10))')
    insert_contacts()


def save_contact(data):
    sql = 'insert into contacts(id,name,contact) values ( %s,%s,%s)'
    val = ( data['id'],data['name'],data['contact'])    
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount," affected")

def get_contact(data):
    sql = "SELECT * FROM contacts WHERE id = %s"
    roll = (data, )
    mycursor.execute(sql, roll)    
    myresult = mycursor.fetchall()

    print(mycursor.rowcount," affected")
    if(mycursor.rowcount == 0):
        return "contact not found check id"
    return myresult

def get_all_contacts():
    sql = "SELECT * FROM contacts"
    mycursor.execute(sql)    
    myresult = mycursor.fetchall()

    print(mycursor.rowcount," affected")    
    return myresult

def get_all_contacts_only():
    sql = "SELECT contact FROM contacts"
    mycursor.execute(sql)    
    myresult = mycursor.fetchall()

    print(mycursor.rowcount," affected")    
    return myresult
    
def delete_contact(id):
    sql = "DELETE FROM contacts WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    if(mycursor.rowcount == 0):
        return "contact not found check id"
    return "Rows affected 1"


    
    