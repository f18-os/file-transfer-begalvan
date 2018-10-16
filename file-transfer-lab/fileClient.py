# client file

import socket
import os

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((socket.gethostname(), 50001))

text_file = 'send_file.txt'

if os.path.isfile(text_file) and os.stat(text_file).st_size != 0:
    # Send file
    with open(text_file, 'rb') as fileserver:
        # Using with, no file close is necessary,
        # with automatically handles file close
        clientsock.send(b'start')
        while True:
            data = fileserver.read(1024)
            print('Sending data', data.decode('utf-8'))
            clientsock.send(data)
            print('Sent data', data.decode('utf-8'))
            if not data:
                print("File is empty now!")
                done = False
                print('Breaking from sending data')
                break
        clientsock.send(b'ENDED')
        fileserver.close()

    # Receive file
    print("Receiving..")
    with open(text_file, 'wb') as fw:
        while True:
            data = clientsock.recv(1024)
            if not data:
                break
            fw.write(data)
        fw.close()
    print("Received..")

    clientsock.close()
else:
    print("No data on file)")
