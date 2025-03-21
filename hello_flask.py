from flask import Flask, render_template, redirect, request
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    return "Flask Working fine"
    
@app.route("/login")
def template():
    return render_template("index.html")
    
@app.route("/pageone")
def pageone():
    return render_template("firstpage.html")
 
@app.route("/pagetwo")
def pagetwo():
    return render_template("secondpage.html")
    
@app.route("/frontpage")
def frontpage():
    return render_template("frontpage.html")
    
@app.route("/resultpage")
def resultpage():
    return render_template("resultpage.html")
    
@app.route("/printtime")
def printtime():
    print()
    print(datetime.datetime.now())
    print()
    return redirect("/resultpage")
    
@app.route("/dashboard")
def dashboard():
    name="kumar"
    notification=5
    mail=8
    
    return render_template("dashboard.html", name_temp=name, notification_temp=notification, mail_temp=mail)

@app.route("/inputpage")
def inputpage():
    return render_template("inputpage.html")
        
@app.route("/statuspage", methods=["GET"])
def statuspage():
    status=request.args.get("textinput")
    return render_template("statuspage.html", status=status)
    
@app.route("/123", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        first_name = request.form.get("name")
        last_name = request.form.get("name2")
        return f"Hello, {first_name} {last_name}! You have successfully logged in."
    return render_template("form.html", author="/123") 
 

        
if __name__=="__main__":
    app.run(port=1245)
    