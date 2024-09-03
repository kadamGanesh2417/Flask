from flask import Flask,render_template,redirect,request,session
import mysql.connector as m_c
# DB = m_c.connect(host="localhost",port= 3306, user="root", password="root1", database="student_mngt")
 
app = Flask(__name__)
app.secret_key= "1233"

@app.route("/session_demo",methods = ["GET","POST"])
def session_demo():
    if request.method == "GET":
        return render_template("session_demo.html")
    else:
        sname = request.form["sname"]
        sEmail = request.form["sEmail"]
        s_cnf_Email = request.form["conf_email"]
        if  sEmail == s_cnf_Email:
            # session["fname"] = sname
            # session["lname"] = sEmail
            sname = request.form["sname"]
            sEmail = request.form["sEmail"]
            scontact = request.form["sContact_num"]
            # con = DB
            # sql = "insert into students(sname,sEmail,sContact_num)values(%s,%s,%s)"
            # cursor = con.cursor()
            # values = (sname,sEmail,scontact)
            # cursor.execute(sql,values)
            # con.commit()
            return f"sname {sname} added successfully"
            
        else:
            return "Email not matched"


        #scontact = request.form["s_Contact_num"]
        
    
    

if __name__ == "__main__":
    app.run(debug=True)
    
