# coding=utf-8
from socket import *
import json,time,yaml
from blockchain import Block,MindNextBlock
from merkle_tree import *
from firstBlock import firstBlock,getMymoney
import threading
import struct
optval = struct.pack("ii", 1, 0)

myPort = 12200
ipPortAlg = ('localhost',12201) # the algorithm port
myIpPort = ('localhost',12200)
ipPortServer = ('localhost',12000) # the communication port


ifFindBlock = threading.Event()
ifRecvNewBlock = threading.Event()
ifFindBlock.clear()
ifRecvNewBlock.clear()

aFindBlock = ''
aRecvBlock = ''
aLastBlock = ''
transactions = [getMymoney(myPort)]

#创建一个短连接,然后发送出去，返回收到的数据
def send(message):
    global clientSocket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_LINGER, optval)
    clientSocket.bind(ipPortAlg)
    clientSocket.connect(ipPortServer)
    clientSocket.send(message)
    receive = clientSocket.recv(10240)
    clientSocket.close()
    return receive


def agrt():
    global a,aFindBlock,aRecvBlock,\
        aLastBlock,ifRecvNewBlock,ifFindBlock,ifRecvNewBlock,transactions
    time.sleep(1)
    # 初始化
    lastBlock = Block()
    lastBlock.parseBlock(aLastBlock)
    mindNextBlock = MindNextBlock(lastBlock)
    mindNextBlock.addTransactions([getMymoney(myPort)])

    while True:
        # 如果没有收到新的block
        if not ifRecvNewBlock.is_set():
            pass
            # 开始挖矿，挖到矿，会进入if语句，进行广播操作
            if mindNextBlock.mineOneStep():
                aFindBlock = mindNextBlock.nextBlock.getBlockStr()

                ifFindBlock.set() #挖到新的block，告诉发送线程来取这个块
                #等待响应
                ifRecvNewBlock.clear()
                ifRecvNewBlock.wait()

                #把最新的block替换进mindNextBlock function
                lastBlock = Block()
                lastBlock.parseBlock(aLastBlock)
                mindNextBlock = MindNextBlock(lastBlock)
                # add new transaction

                mindNextBlock.addTransactions(transactions)
                transactions = []
                transactions = [getMymoney(myPort)]
                ifRecvNewBlock.clear()
        else:
            lastBlock = Block()
            lastBlock.parseBlock(aLastBlock)
            mindNextBlock = MindNextBlock(lastBlock)

            # add new transaction
            mindNextBlock.addTransactions(transactions)
            transactions = []
            transactions = [getMymoney(myPort)]

            ifRecvNewBlock.clear()

def cmnct():
    global a, aFindBlock, aRecvBlock,aLastBlock

    while True:
        # 每次循环创建一个短链接然后询问当前最新的块
        aRecvBlock = send('requestNewBlock')

        # 如果最新块有更新,通知算法线程来拿新的block
        if(aRecvBlock != aLastBlock):
            print('This is the latestBlock')
            print(aRecvBlock)
            aLastBlock = aRecvBlock # 更新当前最新的块
            ifRecvNewBlock.set()
        # 如过发现新的块，则发送给完整节点,然后更新算法
        elif(ifFindBlock.is_set()):

            # 如果收到新的块，则根据新的块重新设置算法
            aRecvBlock = send(aFindBlock)
            aLastBlock = aRecvBlock
            ifRecvNewBlock.set()
            ifFindBlock.clear()

def handleTransRequest():
    global transactions

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(myIpPort)
    serverSocket.listen(1000)

    while (True):
        #
        messageSocket, addr = serverSocket.accept()
        message = messageSocket.recv(10240)
        transactions.append(message)
        messageSocket.send('receive')
        messageSocket.close()
        # 检查格式是否正确






if __name__ == '__main__':

    # 请求获取最新的Node
    aRecvBlock = send('requestNewBlock')
    aLastBlock = aRecvBlock
    lastBlock = Block()
    lastBlock.parseBlock(aLastBlock)
    # build connection to the database server
    t1 = threading.Thread(target=agrt,name="Thread-agrt")
    t2 = threading.Thread(target=cmnct, name="Thread-cmnct")
    t2.start()
    t1.start()

    t3 = threading.Thread(target=handleTransRequest, name="Thread-handleTransRequest")
    t3.start()
