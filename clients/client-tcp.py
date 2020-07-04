import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for tcp connection

#host = '192.168.2.178'
host = socket.gethostname()
port = 4444

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.send("Hello server")

clientsocket.close()

print(message.decode('ascii'))
