# PythonProblems
## 1. Python CRUD API

### FLask based REST API. Run the app.py

### Get All Students
GET localhost:8090/students

### Get student by roll no
GET localhost:8090/student/1

### Add a student
POST localhost:8090/student
<br/>
JSON BODY ->
{
'roll_no':1,
'name':'User1',
'DOB':'2021-10-10',
'contact':'8792684640'
}

### Delete a student by roll no
DELETE localhost:8090/student/1

### Update a student by rol no
PATCH localhost:8090/student/1
<br/>
{
'name':'User2',
'DOB':'2021-10-10',
'contact':'8792684640'
}

## 2. Call Manager Queue

### Contacts being fetched from the DB and loaded into a queue.
### 5 Users are added to a call queue and they are making calls to rnadom number, and for a random duration.
### When a user is done with the call, he will be assigned a queue number and placed at end of queue.

### Run the mainApp.py
