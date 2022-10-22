from flask import Flask
import ibm_db

app=Flask(__name__)
app.secret_key="a"
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCERTIFICATE=DigiCertGlobalRootCA.crt;UID=ygb78843;PWD=kMybE3BM4ArGXlWQ;",'','')

@app.route('/')
def home():   
    return "This File is linked to the DB2 database"

if __name__=="__main__":
    app.run(debug=True)
