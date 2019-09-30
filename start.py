from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import datetime
import json

# mongodb setup
client = MongoClient()
plantdb = client.plantdb
collection = plantdb.plant_collection

# flask setup
app = Flask(__name__)

# root route for plant api
@app.route("/", methods=["GET", "POST"])
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
    app.run(use_reloader=True)
