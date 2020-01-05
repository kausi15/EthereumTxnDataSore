from web3 import Web3, HTTPProvider
from .db_help import store_txn


def get_chain_connection():
    """
    Using this method we can connect to Ethereum chain.
    :return chain_connect:
    """
    chain_url = "https://kovan.infura.io/v3/5e66f831443940ed88e9adca82578c2b"
    check_ = False
    chain_connect = ''
    while not check_:
        chain_connect = Web3(HTTPProvider(chain_url))
        check_ = chain_connect.isConnected()
    return chain_connect


def get_blocks(number_of_latest_blocks):
    """
    Using this method we store the transactions of specified number of latest blocks.
    :param number_of_latest_blocks:
    :return:
    """
    try:
        eth_connect = get_chain_connection()
        max_block_num = eth_connect.eth.blockNumber
        min_block_num = max_block_num - number_of_latest_blocks
        for i in range(min_block_num, max_block_num):
            block_data = eth_connect.eth.getBlock(i, full_transactions=True)
            if len(block_data['transactions']) != 0:
                for z in block_data['transactions']:
                    check_flag_ = False
                    while check_flag_ is False:
                        check_flag_ = store_txn(from_=z['from'], to_=z['to'], block_number=z['blockNumber'],
                                                transaction_hash=z['hash'])
        return True
    except:
        return False

    # It can be another choice for the same method above.
    # for i in range(min_block_num, max_block_num):
    #     #     txn_count = eth_connect.eth.getBlockTransactionCount(i)
    #     #     if not txn_count:
    #     #         continue
    #     #     for z in range(0,txn_count)
    #     #         block_data = eth_connect.eth.getTransactionByBlock(i, z)




