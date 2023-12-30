from flask import Flask, render_template
from flask_pymongo import PyMongo, MongoClient
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config["MONGO_URI"] = "mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net/Flask"
mongo = PyMongo(app)

def get_db_client(host="mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net/Flask", port=27017):
        client = MongoClient(host=host)
        return client

@app.get("/")
def home():
    #create one
    mongo.db.users.insert_one({"username": "Yes"})
    # update one
    mongo.db.users.find_one_and_update({"username": "Yes"}, {"$set": {
        "username": "YEs"
    }})
    # delete one
    mongo.db.users.find_one_and_delete({"username": "YEs"})
    print("Here 2")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")