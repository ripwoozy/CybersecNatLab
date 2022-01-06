import socket
import re
import operator


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('2048.challs.olicyber.it', 10007))
client_socket.settimeout(8.0)

regex = "([A-Z_]*) ([0-9]*) ([0-9]*)"
pattern = re.compile(regex)

operation = {
	"DIVISIONE_INTERA" : operator.__floordiv__,
	"POTENZA" : operator.__pow__,
	"SOMMA" : operator.__add__,
	"DIFFERENZA" : operator.__sub__,
	"PRODOTTO" : operator.__mul__
	}


data = client_socket.recv(1024)

while True:
	print(data)
	data = client_socket.recv(1024)
	data = data.decode()

	if len(data) > 0:
		print(data)
		match = pattern.match(data)
		
		function_to_use = operation[match.group(1)]
		first_param = match.group(2)
		second_param = match.group(3)
				
		print(f"{function_to_use = }", f"{first_param = }", f"{second_param = }", sep='\t')
		
		result = function_to_use(int(first_param), int(second_param))
		
		client_socket.send(str(result).encode())
		client_socket.send(b'\n')
