from socket import *


ipPortAlg = ('127.0.0.1',12001) # the algorithm port
ipPortCmn = ('127.0.0.1',12002) # the communication port

block = 'This is a block'

def mind():
    return True

def add(newblovk):
    return True

if __name__ == '__main__':

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(ipPortCmn)



    # if receive something you can do some process and break the code
    # newblock = sCmnct.recv(1024)
    # if(newblock):
    #     add(newblock)


    if(mind()):
        s.send(block)
        # waiting for the response
        while (True):
            newblock = s.recv(1024)
            if(newblock):
                add(newblock)
                break




