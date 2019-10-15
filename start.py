from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS
import datetime
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
def users():
    if request.method == 'POST':
        data = json.loads(request.data)
        value = data['value']

        if value:
            collection.insert({
                "timestamp": datetime.datetime.now().isoformat(),
                "value": value,
            })
        else:
            return "please provide value"
        return str(value), 201
    else:
        return dumps(collection.find({}))


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0')
