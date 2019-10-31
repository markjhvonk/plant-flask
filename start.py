from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS
import time
import json

# mongodb setup
client = MongoClient()
plantdb = client.plantdb
collection = plantdb.plant_collection

# flask setup
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return "Welcome to the plant-flask-api"

# root route for plant api
@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        data = json.loads(request.data)
        value = data['value']

        if value:
            collection.insert({
                "timestamp": time.asctime(time.localtime(time.time())),
                "value": value,
            })
        else:
            return "please provide value"
        return str(value), 201
    else:
        return dumps(collection.find({}))


@app.route("/latest", methods=["GET"])
def latest():
    return dumps(collection.find().sort([('$natural', -1)]).limit(24))


if __name__ == "__main__":
    # app.run(host='127.0.0.1')
    app.run(host='0.0.0.0')
