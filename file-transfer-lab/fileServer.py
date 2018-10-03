import socket
 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), 50001))
serverSocket.listen(1)
while True:
    (conn, address) = serverSocket.accept()
    text_file = 'fileProj.txt'
 
    #Receive, output and save file
    with open(text_file, "wb") as fw:
        print("Receiving..")
        while True:
            print('receiving')
            data = conn.recv(100)
            if data == b'BEGIN':
                continue
            elif data == b'ENDED':
                print('Breaking from file write')
                break
            else:
                print('Received: ', data.decode('utf-8'))
                fw.write(data)
                print('Wrote to file', data.decode('utf-8'))
        fw.close()
        print("Received..")
 
   