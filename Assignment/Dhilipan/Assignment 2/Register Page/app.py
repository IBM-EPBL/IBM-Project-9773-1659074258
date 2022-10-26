from flask import Flask,request,render_template,session
import ibm_db
import re

app=Flask(__name__)

app.secret_key="a"
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCERTIFICATE=DigiCertGlobalRootCA.crt;UID=ygb78843;PWD=kMybE3BM4ArGXlWQ;",'','')



@app.route('/')
def home():
    return render_template('register.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    Msg=''
    if request.method=='POST':
        UName=request.form['UName']
        UPass=request.form['UPass']
        sql="SELECT * FROM AUsers WHERE UName = ? AND UPass = ?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,UName)
        ibm_db.bind_param(stmt,2,UPass)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        if account:
            session['Loggedin']=True
            # session['id']=account['id']
            session['UNAME']=account['UNAME']
            Msg="Welcome !!! \n Logged in successfully !"
            return render_template('welcome.html',Msg=Msg,UName=UName)
        else:
            Msg="Incorrect Password/Username"
            return render_template('login.html',Msg=Msg)

@app.route('/register/',methods=['POST','GET'])
def register():
    Msg=''
    if request.method=='POST':
        UName=request.form['UName']
        UMail=request.form['UMail']
        UPass=request.form['UPass']
        sql="SELECT * FROM AUsers WHERE UName = ?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,UName)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            Msg="The Account already Exists"
            
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',UMail):
            Msg="Invalid Email Address"
            
        elif not re.match(r'[A-Za-z0-9]+',UName):
            Msg="Name must contain Characters and Numbers"
        else:
            insert_sql="INSERT INTO AUsers VALUES(?,?,?)"
            prep_stmt=ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(prep_stmt,1,UName)
            ibm_db.bind_param(prep_stmt,2,UMail)
            ibm_db.bind_param(prep_stmt,3,UPass)
            ibm_db.execute(prep_stmt)
            Msg="Registered Successfully"
            return render_template('login.html',Msg=Msg)
    elif request.method=='POST':
        Msg="Please Fill the Form"
    return render_template('register.html',Msg=Msg)

if __name__=="__main__":
    app.run(debug=True)
