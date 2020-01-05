from flask import Flask, request, jsonify
from .Helper.db_help import get_txn
from .Helper.eth_helper import get_blocks

application = Flask(__name__)


@application.route('/storeBlocks')
def store_block_txns():
    """
    Using this API, we store the transactions from the specified number of latest blocks.
    :return status of request:
    """
    data = request.get_json()
    number_of_latest_blocks = data['number_of_latest_blocks']
    stored_flag = get_blocks(number_of_latest_blocks=number_of_latest_blocks)
    if not stored_flag:
        return jsonify(status=False, message="Internal Server Error. Try again."), 400
    return jsonify(status=True, message="transactions stored."), 201


@application.route('/getTransactions')
def get_transactions_list():
    """
    Using this API, we can get the list of transactions related to account address passed in parameter.
    :return list of transaction:
    """
    data = request.get_json()
    address = data['address']
    txn_list = get_txn(address)
    if not txn_list:
        return jsonify(status=False, message="Internal Server Error. Try again."), 400
    return jsonify(status=True, message=txn_list), 201


