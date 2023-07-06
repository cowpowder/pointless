import hashlib
import json
from time import time

class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.chain = []

        #creating genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the chain
        param proof: int -> The proof given by the Proof of Work algorithm
        param previous_hash: str -> hash of previous block
        return: dict -> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new txn to enter the next mined block
        param sender: str -> Address of sender
        param recipient: str -> Address of receiver
        param amount: int -> amt of the txn
        return: int -> index of the block that this txn will persist in
        """
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1