import socket

# socket object with socket family and type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #server address
if(host):
  print("got the host name: " + host)
else:
  print("error")

port = 4444 #server port

# binding the server
serversocket.bind((host, port))

# listening to connections up to 3
serversocket.listen(3)

while True:
  clientsocket, address = serversocket.accept()
  print("Received connection from " %str(address))
  message = "Connected to the server" + "\r\n"
  clientsocket.send(message)
  clientsocket.close()
