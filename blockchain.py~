
class Node():
    def __init__(self):
        self.public_key, self.private_key = self.make_wallet()
        self.current_transactions = []
        self.chain = []

    def make_wallet(self):
        pass

    def make_transaction(self, recipient, amount):
        pass

    def mine(self):
        pass

    def validate_chain(self, chain):
        pass

    def getblock(self, node_address):
        pass

    def inv(self):
        pass

    def getdata(self):
        pass

class Block():
    def __init__(self, previous_hash, transactions):
        self.id = None
        self.timestamp = None
        self.previous_hash = previous_hash
        self.current_hash = None
        self.nonce = None
        self.transactions = transactions
        self.merkle_tree = None
        self.summary = {"id": self.id,
                        "timestamp": self.timestamp,
                        "previous_hash": self.previous_hash,
                        "current_hash": self.current_hash,
                        "nonce": self.nonce,
                        "transactions": self.transactions,
                        "merkle_tree": self.merkle_tree}

    def make_merkle_tree(self):
        pass
