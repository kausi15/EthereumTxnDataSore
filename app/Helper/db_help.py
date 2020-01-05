from pymongo import MongoClient
import os


def get_db_connection():

    mongo_uri = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' +\
                os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
    db = MongoClient(mongo_uri)
    return db


def store_txn(from_, to_, block_number, transaction_hash):

    db = get_db_connection()
    try:
        insert_query = {'from': from_, 'to': to_, 'blockNumber': block_number, 'transactionHash': transaction_hash}
        db.txns.insert_one(insert_query)
        return True
    except:
        return False


def get_txn(account_address):

    try:
        db = get_db_connection()
        txn_list = db.performRegex.find({'txns': {'$regex': '^' + account_address + ''}}).pretty()
        return txn_list
    except:
        return False


