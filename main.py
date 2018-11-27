import calendar
import time

from blockchain import *


def main():
    
    # genesis node & block
    GenesisNode = Node()
    GenesisBlock = Block(1, 0, [])
    GenesisBlock.timestamp = 1231006505
    GenesisBlock.previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    GenesisBlock.hash= "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    GenesisBlock.nonce = 2083236893
    
    GenesisNode.chain.append(GenesisBlock)
    
    print(GenesisNode.chain)
    print(GenesisNode.chain[-1].create_summary())
    print(GenesisNode.chain[-1].nonce)

if __name__ == "__main__":
    main()

