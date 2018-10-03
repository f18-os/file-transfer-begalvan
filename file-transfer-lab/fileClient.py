#client file

import socket
 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(), 50001))
 
text_file = 'inputfile.txt'
 
#Sending file
with open(text_file, 'rb') as fs:
    #Using with, no file close is necessary,
    #with automatically handles file close
    clientSocket.send(b'BEGIN')
    while True:
        data = fs.read(1024)
        print('Sending data', data.decode('utf-8'))
        clientSocket.send(data)
        print('Sent data', data.decode('utf-8'))
        if not data:
            print('Breaking from sending data')
            break
    clientSocket.send(b'ENDED')
    fs.close()
 
#Receive file
print("Receiving..")
with open(text_file, 'wb') as fw:
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
print("Received..")
 
clientSocket.close()