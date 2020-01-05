from pymongo import MongoClient
import os


def get_db_connection():
    """
    Using ths method we get a connection with mongodb
    :return db connect:
    """
    mongo_uri = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' +\
                os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
    db = MongoClient(mongo_uri)
    return db


def store_txn(from_, to_, block_number, transaction_hash):
    """
    Usng this method we store the transactions in database.
    :param from_:
    :param to_:
    :param block_number:
    :param transaction_hash:
    :return status of action:
    """
    db = get_db_connection()
    try:
        insert_query = {'from': from_, 'to': to_, 'blockNumber': block_number, 'transactionHash': transaction_hash}
        db.txns.insert_one(insert_query)
        return True
    except:
        return False


def get_txn(account_address):
    """
    Using this we get the list of transactions of specified account address.
    :param account_address:
    :return txn_list:
    """
    try:
        db = get_db_connection()
        txn_list = db.performRegex.find({'txns': {'$regex': '^' + account_address + ''}}).pretty()
        return txn_list
    except:
        return False


