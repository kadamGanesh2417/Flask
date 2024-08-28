from flask import Flask,render_template,redirect,request,session

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
            session["fname"] = sname
            session["lname"] = sEmail
            return  f"session created for {sname} {sEmail}"
        else:
            return "Email not matched"
            

        #scontact = request.form["s_Contact_num"]
        
    
    

if __name__ == "__main__":
    app.run(debug=True)
    
