import socket
import sys


host = 'localhost'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
s.bind((host, port))

print('Server %s on port %s' % (socket.gethostname(), port))

s.listen(1)

while True:
	print('waiting for a connection')
	
	conn, address = s.accept();
while 1:
	print('Connected to %s on port %s ' % (client_address))

	while True:
		data = conn.recv(1024)
		
		reply = 'OK...' + data			
		if not data:
			break
		conn.sendall(reply)