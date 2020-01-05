from pymongo import MongoClient


def get_db_connection():
    """
    Using ths method we get a connection with mongodb
    :return db connect:
    """
    mongo_uri = "Enter the mongodb url here"

    db = MongoClient(mongo_uri)
    return db.test


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
        project = {'from': 1, 'to': 1, 'blockNumber': 1, 'transactionHash': 1, "_id": 0}
        txn_list = db.txns.find({"$or": [{'from': account_address}, {'to': account_address}]}, project)
        return txn_list
    except:
        return False


