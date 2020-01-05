from flask import Flask, request, Response
from app.Helper.db_help import get_txn
from bson import json_util
from app.Helper.eth_helper import get_blocks
import os
import pdb
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
        return Response(
            "Internal Server Error.",
            mimetype='application/json',
            status=400
        )
    return Response(
        "Transaction Stored.",
        mimetype='application/json',
        status=200
    )


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
        return Response(
            "Internal Server Error.",
            mimetype='application/json',
            status=400
        )
    return Response(
        json_util.dumps({'transactions': txn_list}),
        mimetype='application/json',
        status=200
    )


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)

