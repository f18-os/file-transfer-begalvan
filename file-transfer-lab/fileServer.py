# server file

import socket
import os 

num_of_clients = 5 #listen to up to 5 clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 50001))
server.listen(num_of_clients) 
text_file = 'client_' + str(1) + '.txt'

i = 1
while True:
    (conn, address) = serverSocket.accept()
    file_sent = 'sentfile.txt'
 
    #Receive, output and save file
    with open(file_sent, "wb") as fw: # opens file and returns stream
        print("Receiving...")
        while True:
            print("receiving..")
            data = conn.recv(100) #receive up to 100 bytes from the socket
            if data == b'BEGIN': #bytes-BEGIN
                continue
            elif data == b'ENDED':
                print("Breaking from file write")
                break
            else:
                print("Received: ", data.decode('utf-8'))
                fw.write(data)
                print("Wrote to file", data.decode('utf-8'))
        fw.close()

        print("Received")

    #Append and send file
    print("Opening file ", file_sent)
    with open(file_sent, 'ab+') as fa:
        print("Opened file")
        print("Appending string to file.")
        string = b"Append this to file."
        fa.write(string)
        fa.seek(0, 0)
        print("Sending file.")

        while True:
            data = fa.read(1024)
            conn.send(data)
            if not data:
                break
        fa.close()
        print("Sent file.")
    break

serverSocket.close()