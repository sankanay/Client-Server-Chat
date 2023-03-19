
import socket

#create server socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

#declare hostname and port number
host = 'localhost'
port = 5000

#connect to the server
clientSocket.connect((host, port)) 

#print where the client is connected
print("Connected to: ", host, " on port: ", port)

#how to quit
print("Type /q to quit")

#enter message
print("Enter message to send...")

while True:

    #recieve input from client
    clientInput = input(">> ")

    #send input from client
    clientSocket.send(clientInput.encode())

    #if /q is input, then quit
    if clientInput == '/q':
        break

    #receive data from from server
    recData = clientSocket.recv(4096).decode()

    #if /q is recieved, then quit
    if recData == '/q':
        break


    #print recieved data
    print(recData)


clientSocket.close()  # close the connection