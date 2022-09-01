from flask import Flask
from flask_sqlalchemy import SQLAlchemy
mydb = SQLAlchemy()
class Employee(mydb.Model):
    __tablename__ = "Employee"
    id = mydb.Column(mydb.Integer, primary_key=True)
    employee_id = mydb.Column(mydb.Integer(),unique=True)
    name = mydb.Column(mydb.String())
    age = mydb.Column(mydb.Integer())
    position = mydb.Column(mydb.String())
    email = mydb.Column(mydb.String())

    def __init__(self, employee_id, name, age, position,email):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
        self.email = email;

    def __repr__(self):
     return f"{self.name}:{self.employee_id}:{self.position}"
