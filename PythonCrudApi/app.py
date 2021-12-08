# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 00:06:16 2021

@author: ranrakes
"""
from flask import Flask,request,jsonify
import dbService
app = Flask(__name__)

#Craete the database, the tables and populate dummy entries.
dbService.do_setup()

#save a student
@app.route("/student",methods=["POST"])
def add_student():
    data = request.json
    dbService.save_student(data)
    return jsonify(data)

#fetch all the students
@app.route("/students",methods=["GET"])
def fetch_all_students():
    data = dbService.get_all_students()
    return jsonify(data)

#fetch a stduent by roll no
@app.route("/student/<id>",methods=["GET"])
def fetch_student_by_id(id):    
    data = dbService.get_student(id)
    return jsonify(data)

#delete a student by roll no
@app.route("/student/<id>",methods=["DELETE"])
def del_student_by_id(id):
    print(id)
    data = dbService.delete_student(id)
    return jsonify(data)

#update a student by roll no
@app.route("/student/<id>",methods=["PATCH"])
def update_student_by_id(id):
    data = request.json
    data = dbService.update_student(id,data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)