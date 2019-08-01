blockChain = []
pending_transactions = []
owner = "anupunar"

# Watch the earlier videos and add all the required Addons

def get_last_blockchain_value():
    if len(blockChain) < 1:
        return None
    return blockChain[-1] #Returnss the last value of the current BlockChain

def add_transaction(recipient, sender = owner, amount = 0.1): #get_last_blockchain_value()):
    """" Append a new value to the Blockchain

        Args:
            -> sender
            -> recipient
            -> amount - amount of coins
    """
    transaction = {
        'sender' : sender,
        'recipient' : recipient, 
        'amount': amount
        }
    pending_transactions.append(transaction)

def mine_block():
    pass

def get_transaction_value():
    #Returns the user input => The Transaction Amount, as a float
    trx_recipient = input("Enter the recipient of the coins: ")
    trx_amount = float(input("Enter the Transaction amount: ")) #float() is used heere to convert the input into float, as anything passed into the code, using input() --
    # -- is treated as a text
    return trx_recipient, trx_amount #Using paranthesis is optional, when more than one values are retunred as a tuple
    # to return a single item in a tuple, send it as (tx_recipient, )

def get_user_choice():
    user_input = input("Your Choice:")
    return user_input

def print_blockchain():
    # Print the Blockchain
    for block in blockChain:
        print("The current blockchain is: ")
        print(block)
    else:
        print('-' *20)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockChain)):
        if block_index ==  0:
            # The iteration should be skipped if the checking is done on teh 1st block
            continue
        elif blockChain[block_index][0] == blockChain[block_index-1]: # checking if the 1st element of the 2nd block is equal to the entire 1st block
        # blockChain[block_index-1] is used here instead of blockChain[-1], as blockChain[-1] means the last elemnt of the list
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

# Get the 1st transaction and add it ot the blockchain <===> This is out side to the loop to have a way to determine that the chain has an initial values

waiting_for_input = True

while waiting_for_input:
    print("Make your choice \n1) Ad  d a new Transaction \n2) Output the Current Blockchain \nh) Manipulate Block \nq) Quit  \t")
    user_choice = get_user_choice()
    if user_choice=='1':
        trx_data = get_transaction_value()
        recipient, amount = trx_data #Tuple Unpacking => the recipient and amount returned as a tuple, will be mapped--
        # -- approrpiately and stored here
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount = amount) # The named arg amount is used here to skip the optinal param sender, as --
        # -- the value for the sender is already defined
        print(pending_transactions)
    elif user_choice =='2':
        print_blockchain()
    elif user_choice =='h':
        if len(blockChain) >= 1:
            blockChain[0] = [2]
    elif user_choice =='q':
        waiting_for_input = False
    else:
        print("Invalid choice")
    if not verify_chain():
        print_blockchain()
        print("Invalid Blockchain")
        break
    print("Choice Received")
else:
    print("User Left")

print("Done!")