import time
import hashlib
from Crypto.PublicKey import RSA

class Node():
    def __init__(self):
        self.private_key, self.public__key = self.make_wallet()
        self.current_transactions = []   # list of strings
        self.chain = []   # list of block
        self.nodes = set()  # set of network addresses

    def make_wallet(self):
        modulus_length = 1024
        key = RSA.generate(modulus_length)
        pub_key = key.publickey()
        return key, pub_key

    def make_transaction(self, recipient, amount):
        simple_txn = "{} send {} coins to {}".format(self.public_key, amount, recipient)
        self.current_transactions.append(simple_txn)
        return True

    def mine(self, last_block):
        pass
    
    @staticmethod
    def validate_block(self, last_nonce, current_nonce, last_hash):
        ### need double check the inputs
        input = f'{last_nonce}{current_nonce}{last_hash}'.encode()
        input_hash = hashlib.sha256(input).hexdigest()
        return input_hash[:4] == "0000"
        

    def validate_chain(self, chain):
        pass

    def getblock(self, node_address):
        # given node_address, return node.chain
        pass

    def inv(self):
        pass

    def getdata(self):
        pass

class Block():
    def __init__(self, id, previous_hash, transactions):
        self.id = id
        self.timestamp = None
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = None
        self.transactions = transactions
        self.merkle_tree = None

       
    def create_summary(self):
        summary = {"id": self.id,
                        "timestamp": self.timestamp,
                        "previous_hash": self.previous_hash,
                        "current_hash": self.hash,
                        "nonce": self.nonce,
                        "transactions": self.transactions,
                        "merkle_tree": self.merkle_tree}
        return summary

    def make_merkle_tree(self):
        pass


class MerkleTree():
    def __init__(self, transactions):
        self.root = None
        self.parent = None
        self.child = None
