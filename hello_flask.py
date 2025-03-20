from flask import Flask, render_template

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
    
if __name__=="__main__":
    app.run(port=1245)
    