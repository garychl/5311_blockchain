"""
A node to receive data and wirte to database
"""
from socket import *
from sql import *
import json

your_public_ip = None
db_username, db_password, db_name = "root", "password", "blockchainsystem"

serverPort = 22200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((your_public_ip,serverPort))
serverSocket.listen(1)

connection = Connector(db_username, db_password, db_name)
connection.drop_blockchain_table()
connection.create_blockchain_table()

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)

    message = sentence.decode()
    # save message to database
    connection.savetodb(json.loads(message))
    print(message)
    connectionSocket.send('receive'.encode())
    connectionSocket.close()
