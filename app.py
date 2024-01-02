from flask import Flask, render_template
from flask_pymongo import PyMongo, MongoClient
import certifi
app = Flask(__name__)
ca = certifi.where()
app.config["MONGO_URI"] = "mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net/Flask?authSource=admin"
mongo = PyMongo(app, tlsCAFile=ca)

@app.route("/")
def home():
    # #create one
    print(mongo.db.users.insert_one({"Yo": "Hello"}))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)