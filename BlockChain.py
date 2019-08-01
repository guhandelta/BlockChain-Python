blockchain = []

def get_last_blockchain_value():
    #Returns teh last value of the current Blockchain
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    """
        Append a new block into the blockchain

        Arguments:
            1) transaction_amount : The transaction amount to be added into the block
            2) last_transacrion : The last transaction in the blockchian => default([1])

    """
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    #Returns the user input as a float => float() is used to convert the string into float, as the I/P value passed into input()--
    #-- is treated as text
    return float(input('Transaction Amount:'))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)