import socket

# socket object with socket family and type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #server's ip address 192.168.2.178
if(host):
  print("got the host name: " + host)
else:
  print("error")

port = 4444 #server port

# binding the server
serversocket.bind(('192.168.2.178', port))

# listening to connections up to 3
serversocket.listen(3)

while True:
  clientsocket, address = serversocket.accept()
  print("Received connection from %r" % str(address))
  message = "Connected to the server" + "\r\n"
  clientsocket.send(message.encode('ascii'))
  clientsocket.close()
