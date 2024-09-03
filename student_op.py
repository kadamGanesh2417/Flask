from flask import Flask, redirect,render_template,request
import mysql.connector as m_c
DB = m_c.connect(host="localhost",port=3309, user = "root", database="student_mngt", password="@1234")
 
def Add_Student():
    if request.method=="POST":
        sname = request.form["sname"]
        sEmail = request.form["sEmail"]
        scontact = request.form["scontact_num"]
        con = DB
        sql = "insert into students(sname,sEmail,sconatct_num)values(%s,%s,%s)"
        cursor = con.cursor()
        values = (sname,sEmail,scontact)
        cursor.execute(sql,values)
        con.commit()
        return f"sname {sname} added successfully"


    else:
        pass

def Update_Student():
    pass

def GetAllStudents():
    pass

def Remove_student():
    pass
