from blockchain import Block
import hashlib
import json,yaml,time


def getMymoney(port):
    md5 = hashlib.md5()
    message = {}
    message['sender'] = None
    message['receiver'] = 'port_' + str(port)
    message['amount'] = 50
    message['timeStamp'] = str(time.time())
    messageStr= json.dumps(message)
    md5.update(messageStr.encode())
    message['id'] = md5.hexdigest()
    messageStr = json.dumps(message)
    return messageStr

firstBlock = Block(  index=0,
                     nonce=2083236893,
                     last_hash="0000000000000000000000000000000000000000000000000000000000000000",
                     transactions=[getMymoney(12000)],
                     timestamp='1231006505')

if __name__ == '__main__':
    x = yaml.load(firstBlock.getBlockStr())
    print(yaml.load(firstBlock.getBlockStr()))
