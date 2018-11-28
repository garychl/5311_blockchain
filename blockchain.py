
class Node():
    def __init__(self):
        pass

    def getdata(self, hash):
        """ getdata - Request a single block or transaction by hash
        """
        pass

    def inv(self):
        """ inv - "I have these blocks/transactions: ..." Normally sent only when a new block or transaction is being relayed. This is only a list, not the actual data.
        """
        pass
