from socket import*
def handleInv(port):
    global blocksData, blocksIndex
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((('127.0.0.1',port)))
    serverSocket.listen(100)

    while (True):
        #
        clientSocket, addr = serverSocket.accept()
        message = clientSocket.recv(10240)

        print(message)

        clientSocket.send('receive')

if __name__ == '__main__':
    handleInv(12600)