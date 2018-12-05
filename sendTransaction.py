import json,yaml,struct,hashlib,time
from socket import *


optval = struct.pack("ii", 1, 0)

def send(message,nodePort):
    global clientSocket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_LINGER, optval)
    clientSocket.connect(('127.0.0.1',nodePort))
    clientSocket.send(message)
    receive = clientSocket.recv(10240)
    clientSocket.close()
    return receive

def sendTransaction(sender,receiver,amount,nodePort):
    md5 = hashlib.md5()
    message = {}
    message['sender'] = 'port_' + str(sender)
    message['receiver'] = 'port_' + str(receiver)
    message['amount'] = amount
    message['timeStamp'] = str(time.time())
    messageStr= json.dumps(message)
    md5.update(messageStr)
    message['id'] = md5.hexdigest()
    messageStr = json.dumps(message)

    send(messageStr,nodePort)

    print(messageStr)

def getblocks(nodePort):
    recv = send('getData',nodePort)
    recv = yaml.load(recv)
    return recv

def getdata(id,port, type='block'):
    if type == 'block':
        message = {}
        message['type'] = type
        message['id'] = id
        recv = send(yaml.dump(message),port)
        return recv
    elif type == 'transaction':
        message = {}
        message['type'] = type
        message['id'] = id
        recv = send(yaml.dump(message), port)
        return recv

if __name__ == '__main__':
    # recv = getblocks(12001)
    # print(recv)
    # print(len(recv))
    # recv = getdata('52a943c85115424d6534441418a01f9c',12002,type='transaction')
    # print(recv)
    sendTransaction(12300,12400,50,12100)
    sendTransaction(12300, 12400, 50, 12200)