from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('10.0.0.1', 8080))
sock.listen(5)

i = 0
n = 2
arr = ['10.0.0.2','10.0.0.3']

while i < n:
	client_sock, client_addr = sock.accept()
	print("Received connection from : ", client_addr)
	server_sock = socket(AF_INET, SOCK_STREAM)
	server_sock.connect((arr[i], 8000))
	print("Request sent to : ", arr[i])
	i = (i+1)%n
	server_sock.sendall(client_sock.recv(1024))
	client_sock.sendall(server_sock.recv(1024))
	client_sock.close()
	server_sock.close()
