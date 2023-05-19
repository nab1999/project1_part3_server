import os
import random
import hashlib
from socket import *

# set up server
serverPort = 8181
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

# create file with random text data
data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1024))
with open('/serverdata/random_text.txt', 'w') as f:
    f.write(data)

# compute checksum
checksum = hashlib.md5(data.encode()).hexdigest()

while True:
    connectionSocket, addr = serverSocket.accept()

    # send file and checksum
    with open('/serverdata/random_text.txt', 'rb') as f:
        connectionSocket.send(f.read())
    connectionSocket.send(checksum.encode())

    connectionSocket.close()
