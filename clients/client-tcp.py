import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for tcp connection

#host = '192.168.2.178'
host = socket.gethostname()
port = 4444

clientsocket.connect(('192.168.2.178', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
