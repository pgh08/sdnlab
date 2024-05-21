from socket import *

sName = '10.0.0.2'
sPort = 8000
sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.bind((sName, sPort))
sSocket.listen(1)
print("Server is UP and Running")
while True:
	conn, add = sSocket.accept()
	print("Received from : ", add)
	sentence = conn.recv(1024).decode()
	msg = "Hi" + sentence + "from" + sName
	conn.send(msg.encode())
	conn.close()
