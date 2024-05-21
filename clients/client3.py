from socket import *

lname = '10.0.0.1'
lport = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((lname,lport))

sentence = input("Enter your name : ")
clientSocket.send(sentence.encode())
fileContents = clientSocket.recv(1024).decode()
print("From server : ", fileContents)
clientSocket.close()
