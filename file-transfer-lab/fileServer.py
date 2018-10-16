# server file

import socket
import os 

num_of_clients = 5 #listen to up to 5 clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 50001))
server.listen(num_of_clients) 
text_file = 'client_' + str(1) + '.txt'

i = 1
while i <= num_of_clients:
    c, addr = server.accept()
    child_pid = os.fork()
    if child_pid == 0:
        print("\nconnection successful with client " +
                str(i) + str(addr) + "\n")
        while True:
            # name of client in file
            text_file = 'client_' + str(i) + '.txt'

    #Receive, output and save file
    with open(file_sent, "wb") as fw: # opens file and returns stream
        print("Receiving...")
        while True:
            print("receiving..")
            data = c.recv(100) #receive up to 100 bytes from the socket
            if data == b'start': #bytes-start
                continue
            elif data == b'end':
                print("Breaking from file write")
                break
            else:
               decoded_data = data.decode("utf-8")
                if not decoded_data:
                    print("\nconnection with client " + str(i) + " broken\n")
                    print("  CLIENT " + str(i) + " -> " + decoded_data)
                    break

                else:
                    print('Received: ', decoded_data)
                    fw.write(data)
                    print('Wrote to file', decoded_data)
                
        fw.close()

        print("Received")
        decoded_data = data.decode("utf-8")
        if not decoded_data:
            print("\nconnection with client " + str(i) + " broken\n")
            break
        print("  CLIENT " + str(i) + " -> " + decoded_data)

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