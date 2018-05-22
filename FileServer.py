import socket   # networking sockets
import threading    # handle requests from multiple users
import os   # check file size and if exists in directory

def RetrFile(name, sock):  # threading function
    req_size = 2046
    filename = sock.recv(req_size)  # get filename from user
    if os.path.isfile(filename):    # if isFile
        sock.send("EXISTS " + str(os.path.getsize(filename)))   # send bac to client the req file exists and size
        userResponse = sock.recv(req_size)  # wait for user response
        if userResponse[:2] == 'OK' :  # check response input
            print("Transfer started for:" + userResponse)
            with open(filename, 'rb') as f:  # download file 'read binary'
                bytesToSend = f.read(req_size)   # will read specified amount of bytes
                sock.send(bytesToSend)   # send bytes
                while bytesToSend != "":  # if file is larger than req size
                    bytesToSend = f.read(req_size)  # send rest of doc
                    sock.send(bytesToSend)  # send
    else:  # if file doesnt exist
        sock.send("error")   # send error

    sock.close()  # close connect

def main():
    host = '127.0.0.1'  # localhost
    port = 5000  # default port

    s = socket.socket()  # create socket
    s.bind((host, port))  # bind socket to host and port

    s.listen(5)  # listen for up to 5 connections

    print "Server running.."
    while True:
        c, addr = s.accept()  # identify connected clients
        print "New client connected: <" + str(addr) + ">"  # print on console
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))  # create thread
        t.start()  # handle incoming connections

    s.close()

if __name__ == '__main__':
    main()
