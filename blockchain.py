
class Node():
    def __init__(self):
        pass

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
        

class Block():
    def __init__(self):
        pass
