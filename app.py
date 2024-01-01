from flask import Flask, render_template
import pymongo, certifi, ssl
ca = certifi.where()
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
mongo_url = "mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net/Flask?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url, tls=True, tlsAllowInvalidCertificates=True, tlsCAFile=certifi.where())
db = client["Flask"]

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

@app.get("/")
def home():
    # #create one
    print(db["users"].insert_one({"Username": "Eitan", "password": "Random"}))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)