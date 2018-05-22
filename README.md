## Nets tcp file transfer

Program utilized TCP to safely tranfer files from server through client. 

#### Server:
Accepts requests from up to 5 clients and will transfer requested files to client if file is available.

#### Client:
Requests files from server and if file exists, after accepting transfer will begin receiving file.

#### To use:
* Run FileServer.py through command line followed by up to 5 FileClient.py
* After connecting client you can request either a text file or image through the command line (ex. file.txt or image.jpeg)
* Client will close after file has been transferred successfully

Resources: [Youtube] Python Advanced Tutorial 6.6 - Simple File Server
https://youtu.be/LJTaPaFGmM4

---

##### nets-tcp-file-transfer

For this lab, you must define a file transfer protocol and implement a client and server.  The server must be 
* single-threaded, 
* and accept multiple concurrent client connections.   

Like the demo code provided for this course, your code 
* should be structured around a single loop with a single call to select(), 
* and all information about protocol state should be explicitly stored in variables 

Recall that unlike UDP, which is a message-oriented protocol, TCP is stream-oriented.  

A practical implication of this difference is that the outputs of multiple writes may be concatenated and reads may only 
return a portion of the data already sent.  You are strongly encouraged to test your implementation using the stammering
proxy from https://github.com/robustUTEP/nets-tcp-proxy.git

