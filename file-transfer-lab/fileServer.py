#server file

import socket
import os 

 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), 50001))
serverSocket.listen(5) #listen to up to 5 clients

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

def handle_client(serverSocket, address, id):
    while True:
        data=serverSocket.recv(1024)
        decoded_data=data.decode("utf-8")
        if not decoded_data:
                print("\nconnection with client " + str(id) + " broken\n")
                break
        print("  CLIENT " + str(id) + " -> " + decoded_data)

def server():
    i=1
    while 1<=5:
        conn, address = serverSocket.accept()
        child_pid = os.fork()
        if child_pid == 0:
            print("\nConnection with client successful")
            break
        else:
            i += 1

server()

serverSocket.close()