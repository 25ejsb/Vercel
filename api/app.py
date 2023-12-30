from flask import Flask, render_template
from flask_pymongo import PyMongo, MongoClient
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net"
mongo = PyMongo(app)

def get_db_client(host="mongodb+srv://eitanbrochstein:25Greenseed@cluster0.rhtkmvj.mongodb.net", port=27017):
        client = MongoClient(host=host)
        return client

@app.route("/")
def home():
    # create one
    # try:
    #     client = get_db_client()
    #     db = client["Flask"]
    #     db.users.insert_one({"username": "Yes"})
    #     # update one
    #     db.users.find_one_and_update({"username": "Yes"}, {"$set": {
    #         "username": "YEs"
    #     }})
    #     # delete one
    #     db.users.find_one_and_delete({"username": "YEs"})
    #     print("Here")
    #     return render_template("index.html")
    # except:
    #     print("Here 2")
    #     return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")