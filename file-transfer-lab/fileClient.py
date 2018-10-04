#client file

import socket
import os
 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((socket.gethostname(), 50001))
 
file_sent = 'textfile.txt'

if os.path.isfile(file_sent) and os.stat(file_sent).st_size !=0:
    with open(file_sent, 'rb') as fs: #send textfile, handles file close
        clientSocket.send(b'START ')
        while True:
        data = fs.read(1024)
        print('Transfering file', data.decode('utf-8')) #uses UTF-8 enconding
        clientSocket.send(data)
        print('File sent', data.decode('utf-8'))
        if not data:
            print('Breaking from transfering file')
            break
    clientSocket.send(b'END ')
    fs.close()
 
#Receive file
print("Receiving..")
with open(file_sent, 'wb') as fw:
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
print("Received..")
 
clientSocket.close()