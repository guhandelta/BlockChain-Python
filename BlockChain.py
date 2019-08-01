blockchain = []

def get_last_blockchain_value():
    #Returns teh last value of the current Blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1] # if the if condition is met, the fn() is quit automatically and so-
    #- this statement is not included in an else block

def add_transaction(transaction_amount, last_transaction=[1]): #last_transaction=[1] is not removed as it is a required param
    """
        Append a new block into the blockchain

        Arguments:
            1) transaction_amount : The transaction amount to be added into the block
            2) last_transacrion : The last transaction in the blockchian => default([1])

    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    #Returns the user input as a float => float() is used to convert the string into float, as the I/P value passed into input()--
    #-- is treated as text
    user_input = float(input('Transaction Amount:'))
    return user_input

def get_user_choice():
    user_input = input('User Choice:\t')
    return user_input

def print_blockchain():
 #Output the Blockchain list
    for block in blockchain:
        print("Printing the Blockchain", block)    

# Get the 1st transaction and add it to the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

while True:
    print("Make your choice \n1) Add a new Transaction \n2) Output the blockchain \nq) Quit" )
    user_choice = get_user_choice() 

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice=='q':
        break
    else:
        print("Invalid Entry")

print("Done!")