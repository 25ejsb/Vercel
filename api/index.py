from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net/Flask"
mongo = PyMongo(app)

@app.route("/")
def home():
    # create one
    mongo.db.users.insert_one({"username": "Yes"})
    # update one
    mongo.db.users.find_one_and_update({"username": "Yes"}, {"$set": {
        "username": "YEs"
    }})
    # delete one
    mongo.db.users.find_one_and_delete({"username": "YEs"})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)