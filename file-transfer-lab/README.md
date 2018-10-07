# File Transfer Lab

Directory `file-transfer-lab` includes: 
fileClient.py, fileServer.py, stammerProxy.py and textfile.txt

*   `fileClient.py` transfers a file to the server using port 50001

*   `fileServer.py` receives a file from client -up to 100 bytes from the socket at a time- listening on port 50001

*   `stammerProxy.py` forwards tcp streams. It may delay the transmission of data but ensures all data will be forwarded, eventually.
   By default,
   it listens on port 50000 and forwards to localhost:50001.  Use the -?
   option for help.

The client-server files can be tested with or without and without the proxy

To use files without proxy: 

* 1. Open fileServer.py:

        python3 fileServer.py

* 2. Open fileClient.py:

        python3 fileClient.py

    client will immediately send textfile.txt to server, server will receive up to 100 bytes at a time
form socket and will write data to create new file

To use files with proxy: 

* 1. Open fileServer.py:

        python3 fileServer.py

* 2. Open stammerProxy.py:  

        python3 stammerProxy.py

* 3. Open fileClient.py:

        python3 fileClient.py -s localhost:50001

        client will immediately send textfile.txt to proxy listening on port 50000, proxy listening on port 50000 will get file and transfer to server listening on port 50001