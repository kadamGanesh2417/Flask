from flask import Flask, redirect,render_template,request
import mysql.connector as m_c
DB = m_c.connect(host="localhost",port=3306, database="studenet_mngt", password="@1234")
 
def Add_Student():
    if request.method=="GET":
        pass
    else:
        pass

def Update_Student():
    pass

def GetAllStudents():
    pass

def Remove_student():
    pass
