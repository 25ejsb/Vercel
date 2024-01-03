from flask import Flask, render_template
from flask_pymongo import PyMongo, MongoClient
import certifi
app = Flask(__name__)
ca = certifi.where()
app.config["MONGO_URI"] = "mongodb+srv://ebroch:25Greenseed@flask.01kp9mt.mongodb.net/Flask?authSource=admin&tlsCAFile=ca"
mongo = PyMongo(app)

@app.route("/")
def home():
    # #create one
    print(mongo.db.users.insert_one({"Yo": "Hello"}))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)