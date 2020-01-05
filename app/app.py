import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

application = Flask(__name__)
application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD']\
                                  + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongodb = PyMongo(application)
db = mongodb.db


@application.route('/getTransactions')
def get_transactions_list():
    data = request.get_json()
    address = data['address']
    txn_list = db.performRegex.find({'txns': {'$regex': '^'+address+''}}).pretty()
    return jsonify(status=True, message=txn_list), 201


