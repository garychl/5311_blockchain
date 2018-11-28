from blockchain import Block, Node

NodeA = Node()
NodeA.make_transactions("address_of_B", 100)
print(NodeA.transactions)
