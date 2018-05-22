import socket

def main():
    host = '127.0.0.1'  # tuple local host
    port = 5000  # default port
    req_size = 2046

    s = socket.socket()  # create tcp socket
    s.connect((host, port))  # connect host and port

    filename = raw_input("Filename? ->")  # user input
    if filename != 'quit!':  # quits if user input matches command
        s.send(filename)
        data = s.recv(req_size)  # var data stores if exists or not
        # if requested file exists
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])  # shows filesize to user
            # prints message to console if file exists and options
            message = raw_input("File found, size: " + str(filesize) + "bytes. \n To download send (Y/N)? ->")
            if message.upper() == 'Y':  # if download accepted
                s.send('OK')  # send OK signal
                f = open(' new_'+filename, 'wb')  # append new to filename
                data = s.recv(req_size)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:    # if total is greater continue downloading
                    data = s.recv(req_size)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"  # special message displaying info
                print "Download Complete!"
        else:
            print "file does not exist"
    s.close()

if __name__ == '__main__':
    main()
