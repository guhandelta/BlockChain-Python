blockchain = []

#Function to retrieve the previous block's value
def get_last_blockchain_value():
    #Returns teh last value of the current Blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1] # if the if condition is met, the fn() is quit automatically and so-
    #- this statement is not included in an else block

#Function to add a new transaction
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

#Function to recieve the Transaction value
def get_transaction_value():
    #Returns the user input as a float => float() is used to convert the string into float, as the I/P value passed into input()--
    #-- is treated as text
    user_input = float(input('Transaction Amount:\t'))
    return user_input

#Function to get the Users's choice of action
def get_user_choice():
    user_input = input('User Choice:\t')
    return user_input

#Function to print the entire blockchain
def print_blockchain():
 #Output the Blockchain list
    print('-' * 20, '\n The Blockchain: \n')
    for block in blockchain:
        print("Printing the Blockchain", block)    
    else:
        print('-' * 20)

#Function to verify if the chain is valid
def verify_chain():
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            #block_index += 1 # Security feature for checking the previous block for 1st node
            continue #skip the following lines and proceed with the iteration
        if blockchain[block_index][0] == blockchain[block_index -1]:
            is_valid = True
        else:
            is_valid = False
            break
    #     block_index += 1
    return is_valid
            

# Get the 1st transaction and add it to the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

waiting_for_input = True

while waiting_for_input:
    print("Make your choice \n1) Add a new Transaction \n2) Output the blockchain \nh) Manipulate Blockchain \nq) Quit" )
    user_choice = get_user_choice() 

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice=='h':
        if len(blockchain) >=1:
            blockchain[0] = [2]
        print("Cannot Manipulate a Block")
    elif user_choice=='q':
        waiting_for_input = False
    else:
        print("Invalid Entry")
    if not verify_chain():
        print_blockchain()
        print("Invalid Entry")
        break
else:
    print("User Left")

print("Done!")