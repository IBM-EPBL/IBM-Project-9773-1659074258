from flask import render_template,Flask,request

app=Flask(__name__)
@app.route("/")

def index():
    return render_template("register.html")

@app.route("/Register", methods=["POST","GET"])

def Register():
     if request.method=="POST":
         name=request.form.get('name')
         age=request.form.get('age')
         mail=request.form.get('mail')
         qual=request.form.get('qual')
         return render_template("result.html",name=name,age=age,mail=mail,qual=qual )

if __name__=='__main__':
    app.run(debug=True)   
