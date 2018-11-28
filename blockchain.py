import time
import hashlib
from Crypto.PublicKey import RSA

class Block(object):

    def __init__(self, index, proof, previous_hash, transactions, timestamp=None):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()

    @property
    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)



class Node(object):
    def __init__(self):
        self.private_key, self.public_key = self.make_wallet()
        self.chain = []
        self.transactions = []
        self.nodes = set()

    def make_wallet(self):
        modulus_length = 1024
        key = RSA.generate(modulus_length)
        pub_key = key.publickey()
        self.address = pub_key
        return key, pub_key

    def getdata(self, hash):
        """ getdata - Request a single block or transaction by hash
        return: block or txn
        """
        pass

    def inv(self):
        """ inv - "I have these blocks/transactions: ..." Normally sent only when a new block or transaction is being relayed. This is only a list, not the actual data.
        """
        pass

    def getblocks(self):
        """getblocks - Request an inv of all blocks in a range
        return: list of blocks in a range
        """

    def make_transactions(self, recipient, amount):
        self.transactions.append(
            {"sender":self.address,
             "recipient":recipient,
             "amount":amount})
        return True
