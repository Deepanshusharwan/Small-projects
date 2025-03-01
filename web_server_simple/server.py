#a simple web server with some error checking

from socket import *


def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)#here we make a socket #this makes the phone for the phone call just like it did in the case of the browser but here the call will be made to the server
    try:
        serverSocket.bind(('localhost', 9000))#binds the socket to the port 9000 on the localhost (note: a port can't be used by more then one software at once if you try to run another software on port 9000 then it will give you an error sayn gthat the address is already in use
        serverSocket.listen(5)#defines khow many calls t can take like here it says that if it is busy taking a server request the os should queue 4 more calls at once for it to handle when it is done with the current one
        #if we didn't specify this then the server wouldn't have been able to handle more then one request
        while(1):#starts an infinite loop
            (clientSocket, addr) = serverSocket.accept()#this blocks the further execution of the script until a call is made
            #when a call is made it returns a tuple containing a socket object(clientSocket here) and the ip address along with the port (addr in the above line)

            rd = clientSocket.recv(5000).decode()#according to the http protocol the client must speak first so here we are recieving
            #the recieve is a two way street in http protocol first the server listens for any requests by the client and recieves it
            #then the server sends the data packet and the browser receive the data
            #here we have specified that we want the requests by the browsers to be at most 5000 bytes long and then decode it from utf-8 to unicode
            pieces = rd.split("\n")#
            if len(pieces) > 0: print(pieces[0])#this server looks at the first line of the request and prints it in the console

            data = "HTTP/1.1 200 OK\r\n"#this is the response of the server to the client
            #it tells the browser what the status of the request is
            data += "Content-Type: text/html; charset=utf-8\r\n"#this line tells the browser what type of data we are sending
            data += "\r\n"
            data += "<html><body><h1>Hello World</h1></body></html>"#here we send a web page as a response
            clientSocket.sendall(data.encode())#endoding the data packet and then sending it to the client
            clientSocket.shutdown(SHUT_WR)#after the servers work is done it closes the connection and waits for another connection to be made

    except KeyboardInterrupt:#handles the exceptions that the server faces
        print("\nShutting down...\n")

    except Exception as exc:
        print(f"ERROR: \n{exc}")

    serverSocket.close()

print("Access http://localhost:9000")#here we specify the the address of the server for easy access
createServer()#starts the server




