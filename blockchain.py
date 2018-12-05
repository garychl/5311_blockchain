import time
import json
import yaml,random
import hashlib
from merkle_tree import *
from Crypto.PublicKey import RSA

# import mysql.connector


class Block(object):
    def __init__(self, index='', nonce='', last_hash='',transactions=None, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.last_hash = last_hash
        self.transactions = transactions
        if transactions == None:
            self.merkleRoot = '0'
        else:
            self.merkleRoot = MerkleTree(transactions).root.data

        self.timestamp = timestamp or time.time()

    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.nonce, self.last_hash, self.merkleRoot, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def parseBlock(self,blockstr):
        print("~~~~~~~",blockstr)
        jsonBlock = yaml.safe_load(blockstr)
        print(jsonBlock)
        self.index = jsonBlock['index']
        self.nonce = jsonBlock['nonce']
        self.last_hash = jsonBlock['last_hash']
        self.timestamp = jsonBlock['timestamp']
        self.transactions = jsonBlock['transactions']
        self.merkleRoot = jsonBlock['merkleRoot']

        return self

    def getBlockDict(self):
        dict = {}
        dict['index'] = self.index
        dict['nonce'] = self.nonce
        dict['last_hash'] = self.last_hash
        dict['timestamp'] = self.timestamp
        dict['transactions'] = self.transactions
        dict['merkleRoot'] = self.merkleRoot

        return dict

    def getBlockStr(self):

        return yaml.dump(self.getBlockDict())




class MindNextBlock():
    def __init__(self,lastBlock):
        self.lastBlock = lastBlock
        self.nextBlock = Block()
        self.nextBlock.index = lastBlock.index + 1
        self.nextBlock.last_hash = lastBlock.get_block_hash()
        self.nextBlock.timestamp = str(time.time())
        self.nextBlock.nonce = random.randint(-1,999999) # or random number
        self.guess = 0
        self.guess_hash = 0

    def valid_proof(self, difficulty=5):
        """Validates the Proof
        :param last_nonce: <int> Previous Proof
        :param nonce: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.
        """
        self.guess = '{}{}{}{}{}'.format(self.nextBlock.index,
                                    self.nextBlock.nonce,
                                    self.nextBlock.last_hash,
                                    self.nextBlock.merkleRoot,
                                    self.nextBlock.timestamp).encode()
        self.guess_hash = hashlib.sha256(self.guess).hexdigest()
        return self.guess_hash[:difficulty] == "0" * difficulty


    def mineOneStep(self):

        self.nextBlock.nonce += 1
        result = self.valid_proof()

        return result
    def addTransactions(self,transactions):

        self.nextBlock.transactions =  []
        # deep copy
        for transaction in transactions:
            self.nextBlock.transactions.append(transaction)
        tree =  MerkleTree(self.nextBlock.transactions)
        self.nextBlock.merkleRoot = tree.root.data

# class GenesisBlock(Block)
