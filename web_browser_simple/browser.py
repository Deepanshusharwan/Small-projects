#WORLD'S SIMPLEST BROWSER
import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sets up  a socket on our end (kinda like it sets up the phone in a phone call)
#the above line to create a socket is not changed and is used to establish sockets on our end and it won't ever show error unless the machine doesn't support networking whihc is highly unlikely these days

mysock.connect(("data.pr4e.org", 80))#this makes the phone call i.e connects our socket to the domain on the supplied port
cmd = "GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n".encode()#here we specify the command we want to send to the server and and we sended it encoded in the "utf-8" format as normally python encodes stuff in unicode format and utf-8 is more densely packed and useed by serverss

mysock.send(cmd)#here we send the command to the server
#as this is the networking in this case it according to the protocol we first have to send a request to be able to communicate with the server
while True:
    data = mysock.recv(512)#here we receive the data from the server and wait for it until the server is done sending data for the data reaches the 512 character limit as specified by us then python moves on to the next step
    if len(data) < 1:#if we don't receive any data form the server meaning the data length is less than 1 it means the server has been shut down and we break our loop here
        break
    print(data.decode(),end='')#here we decode the utf-8 data back into the unicode
    #here we use the end = ''  so that in our data instead of it being like "Not Found\r\n" it would be like "Not Found \r \n" and it can be properly formatted in the terminal
mysock.close()
#closes the socket and so as to prevent any security breach

