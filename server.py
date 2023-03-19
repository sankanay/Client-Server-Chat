import socket

#create server socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

#declare hostname and port number
host = 'localhost'
port = 5000

#bind socket with host/port
serverSocket.bind((host, port))

#listen for client
serverSocket.listen(1)

#print where the server is listening
print("Server listening on: ", host, " on port: ", port)

#establish connection
conn, addr = serverSocket.accept()

#print conencted by
print("Connected by", addr)

#wait for message
print("Waiting for message...")

#loop to recieve data
while True:

    #receive data from client
    recData = conn.recv(4096).decode()

    #if /q is recieved, then quit
    if recData == '/q':
        break

    #exit loop if not data is recieved
    if not recData:
        break

    #print recieved data
    print(recData)

    #how to quit
    print("Type /q to quit")

    #prompt input
    print("Enter message to send...")

    #recieve input from server
    serverInput = input(">> ")

    #send message server message to client
    conn.send(serverInput.encode())

    #if /q is input, then quit
    if serverInput == '/q':
        break

conn.close()


