# Initializing our blockchain list
from typing import List


blockchain: List = []


def get_last_block_value():
    """ Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the las blockchain value to the blockchain. 

    Arguments:
        :transaction_amount: The amount that should be added.

        :last_transaction: The last blockchain transaction (default [1]).s
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the suer (a new transaction amount) as a float"""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


# Output the blockchain list to the console
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)



def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transacion value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_block_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the')
    if not verify_chain():
        print('Invalid blockchain!')
        break

    print('Choice registered!')
else:
    print('User left!')


print('Done!')
