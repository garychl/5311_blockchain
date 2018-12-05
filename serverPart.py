# coding=utf-8
from firstBlock import firstBlock
from socket import *
import json,time,yaml
from blockchain import Block,MindNextBlock
from merkle_tree import *
from firstBlock import firstBlock
import threading
import struct
from util import *
optval = struct.pack("ii", 1, 0)

blocksData = []
blocksIndex = {}

### The first Node and Block
# "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f" is the true hash for GenesisBlock

latestNodeStr = firstBlock.getBlockStr()
blocksIndex[firstBlock.get_block_hash()] = 0
blocksData.append(latestNodeStr)


print(latestNodeStr)

print('hash is %s ' % firstBlock.get_block_hash())
runserver_port = ('localhost', 12000) # this port is run server use
handlegetblocks_port = ('localhost', 12001) # this port is handle get data use
handlegetdata_port = ('localhost', 12002) # this port is handle get data use

def runserver():
    global latestNodeStr,blocksData
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(runserver_port)
    serverSocket.listen(100)

    while (True):
        #
        clientSocket, addr = serverSocket.accept()
        message = clientSocket.recv(10240)
        if message == 'requestNewBlock':
            clientSocket.send(latestNodeStr)
            clientSocket.close()
        else:
            # 验证区块是否正确
            if verifyBlock(message, latestNodeStr):
            # 更新块
                latestNodeStr = message
                newBlock = Block()
                newBlock.parseBlock(latestNodeStr)


                # 加入dataBase
                xx = yaml.load(latestNodeStr)


                ###
                last_hash = newBlock.get_block_hash()
                blocksData.append(newBlock.getBlockStr())
                blocksIndex[last_hash] = len(blocksData) - 1

                print(latestNodeStr)
                print('hash is %s ' % last_hash)


            # 发送当前最新的块回去
            clientSocket.send(latestNodeStr)
            clientSocket.close()

def handleGetBlocks():
    global blocksData,blocksIndex
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(handlegetblocks_port)
    serverSocket.listen(100)

    while (True):
        #
        clientSocket, addr = serverSocket.accept()
        message = clientSocket.recv(10240)
        message = []
        for hash in blocksIndex:
            message.append(hash)
        clientSocket.send(yaml.dump(message))

def handleGetData():
    global blocksData,blocksIndex
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(handlegetdata_port)
    serverSocket.listen(100)

    while (True):
        #
        clientSocket, addr = serverSocket.accept()
        message = clientSocket.recv(10240)
        message = yaml.load(message)
        if(message['type'] == 'block'):
            index = blocksIndex[message['id']]
            blocksData[index]
            clientSocket.send(blocksData[index])

        elif(message['type'] == 'transaction'):
            recv= 'nothing'
            for block in blocksData:
                parseBlock = yaml.load(block)
                for transaction in parseBlock['transactions']:
                    parseTransaction = yaml.load(transaction)
                    if parseTransaction['id']==message['id']:
                        recv = yaml.dump(parseTransaction)
            clientSocket.send(recv)
def inv(port):
    global blocksData, blocksIndex
    while True:
        time.sleep(1)

        # blocks
        message = {}
        hashlist = []
        for hash in blocksIndex:
            hashlist.append(hash)
        message['items'] = hashlist
        message['types'] = 'block'
        message['AddrFrom'] = 12000

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.setsockopt(SOL_SOCKET, SO_LINGER, optval)
        clientSocket.connect(('localhost', port))
        clientSocket.send(yaml.dump(message))
        receive = clientSocket.recv(10240)
        clientSocket.close()

        time.sleep(5)

        # blocks
        message = {}
        hashlist = []

        for block in blocksData:
            parseBlock = yaml.load(block)
            for transaction in parseBlock['transactions']:
                parseTransaction = yaml.load(transaction)
                hashlist.append(parseTransaction['id'])

        message['items'] = hashlist
        message['types'] = 'transaction'
        message['AddrFrom'] = 12000

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.setsockopt(SOL_SOCKET, SO_LINGER, optval)
        clientSocket.connect(('localhost', port))
        clientSocket.send(yaml.dump(message))
        receive = clientSocket.recv(10240)
        clientSocket.close()



if __name__ == '__main__':

    t1 = threading.Thread(target=runserver, name="Thread-runserver")
    t1.start()
    t2 = threading.Thread(target=handleGetBlocks, name="Thread-handleGetBlocks")
    t2.start()
    t3 = threading.Thread(target=handleGetData, name="Thread-handleGetData")
    t3.start()

    # inv(12600)
