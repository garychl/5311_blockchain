from blockchain import Block, Node

### The first Node and Block
GenesisNode = Node()
GenesisBlock = Block(index=0,
                     nonce=2083236893,
                     last_hash="0000000000000000000000000000000000000000000000000000000000000000",
                     transactions=0,
                     timestamp=1231006505)
# "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f" is the true hash for GenesisBlock
GenesisNode.chain.append(GenesisBlock)
GenesisNode.mine()

### Modelling the real world
NodeA = Node()
NodeA.chain.append(GenesisBlock)  # pretend we receive block data from other node
NodeA.make_transactions("address_of_B", 100)
NodeA.mine()

