from merkle_tree import*
from blockchain import Block,MindNextBlock
def verifyBlock(blockStr,latestblockStr,difficulty=5):

    block = Block().parseBlock(blockStr)
    latestbBlock = Block().parseBlock(latestblockStr)

    merkleRoot = MerkleTree(block.transactions).root.data
    if not merkleRoot == block.merkleRoot:
        return False
    if not latestbBlock.get_block_hash() == block.last_hash:
        return False
    if not block.get_block_hash()[:difficulty] == "0" * difficulty:
        return False
    return True