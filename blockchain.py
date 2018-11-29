import time
import hashlib
from Crypto.PublicKey import RSA

# import mysql.connector


class Block(object):
    def __init__(self, index, nonce, last_hash, transactions, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.last_hash = last_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()

    @property
    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.nonce, self.last_hash, self.transactions, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return "index:{} - nonce:{} - last_hash:{} - transactions:{} - timestamp:{}".format(self.index, self.nonce, self.last_hash, self.transactions, self.timestamp)


# class GenesisBlock(Block)

class Node(object):
    def __init__(self):
        self.private_key, self.public_key = self.make_wallet()
        self.chain = []
        self.transactions = []
        self.nodes = set()

#    def connect_db(self, username, password, dbname, host="localhost"):
#        self.mydb = mysql.connector.connect(
#            host=host,
#            user=username,
#            passwd=password,
#            database=dbname
#        )
#        self.mycursor = self.mydb.cursor()
#        return True

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
        pass

    def make_transactions(self, recipient, amount):
        self.transactions.append(
            {"sender":self.address,
             "recipient":recipient,
             "amount":amount})
        return True

    @staticmethod
    def valid_proof(index, nonce, last_hash, transactions, timestamp, difficulty=4):
        """Validates the Proof
        :param last_nonce: <int> Previous Proof
        :param nonce: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.
        """
        guess = f'{index}{nonce}{last_hash}{transactions}{timestamp}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == "0"*difficulty

    def proof_of_work(self, index, last_hash, transactions, timestamp):
        nonce = 0

        while not self.valid_proof(index, nonce, last_hash, transactions, timestamp):
            nonce += 1

        return nonce

    def create_new_block(self, index, nonce, last_hash, transactions, timestamp):
        block = Block(
            index=index,
            nonce=nonce,
            last_hash=last_hash,
            transactions=transactions,
            timestamp=timestamp
        )
        self.transactions = []  # Reset the transaction list
        self.chain.append(block)
        return block

    def mine(self):
        # omit: send rewards to miner
        index = len(self.chain)
        last_block = self.chain[-1]
        last_hash = last_block.get_block_hash
        transactions = self.transactions
        timestamp = time.time()
        nonce = self.proof_of_work(index, last_hash, transactions, timestamp)

        block = self.create_new_block(index, nonce, last_hash, transactions, timestamp)
        print("Successfully mined a block! \nblock details:", block)
        print("Block hash is: {}".format(block.get_block_hash))
        return True
