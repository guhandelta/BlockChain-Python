blockchain = []
pending_transactions = []
owner = "anupunar"

#Function to retrieve the previous block's value
def get_last_blockchain_value():
    #Returns teh last value of the current Blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1] # if the if condition is met, the fn() is quit automatically and so-
    #- this statement is not included in an else block

#Function to add a new transaction
def add_transaction( recipient, sender=owner, amount=1.0): #last_transaction=[1] is not removed as it is a required param
    # sender and amount are optin args, as the values are already specified, so recipient is placed first
    """
        Append a new block into the blockchain

        Arguments:
            1) Sender : The sender of the coins
            2) Recipient : The recipient of the coins
            3) Amount : The amount of coins sent in the transaction => default([1])

    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
        }
    pending_transactions.append(transaction)

def mine_block():
    pass

#Function to recieve the Transaction value
def get_transaction_value():
    #Returns the user input as a float => float() is used to convert the string into float, as the I/P value passed into input()--
    #-- is treated as text
    tx_recipient = input('Enter the recipient of the coins:\t')
    tx_amount = float(input('Transaction Amount:\t'))
    return tx_recipient, tx_amount #Return these 2 values as/in a tuple
    # return (tx_recipient, tx_amount) => () is optional for tuples with multiple values

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

waiting_for_input = True

while waiting_for_input:
    print("Make your choice \n1) Add a new Transaction \n2) Output the blockchain \nh) Manipulate Blockchain \nq) Quit" )
    user_choice = get_user_choice() 

    if user_choice == '1':
        tx_data = get_transaction_value() #This fn() returns the transaction data
        recipient, amount = tx_data #Tuple unpacking => stores recipient value from tuple, in recipient var ann same for the amount
        add_transaction(recipient, amount=amount)# The named arg amount allows to skip using the sender arg, which is already populated
        print(pending_transactions) # Print the pending transactions, after the add_transaction call
    elif user_choice == '2':
        print_blockchain()
    elif user_choice=='h':
        if len(blockchain) >=1:
            blockchain[0] = [2]
        print("Cannot Manipulate a Block")
        waiting_for_input = False
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