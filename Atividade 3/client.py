import socket
import sys

host = 'localhost'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print("Para sair use CTRL+X e pressione enter\n")
msg = input()

	
while (msg != '\x18'):			
	# Envia os dados
	s.sendall(msg)
	
	#recebe a resposta do servidor
	data = s.recv(1024)
	print (data)