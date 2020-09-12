import socket
import argparse
import threading 
import requests

parser = argparse.ArgumentParser(description = "Multithread so o básico")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = 'localhost')
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 8080)
args = parser.parse_args()

print(f"Server rodando {args.host} na porta {args.port}")

socketDosCria = socket.socket()
socketDosCria.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	socketDosCria.bind((args.host, args.port))
	socketDosCria.listen(5)
except Exception as e:
	raise SystemExit(f"Não é possivel escuta: {args.host} na porta: {args.port}, por esse: {e}")


def clienteNovo(cliente, connection):
	ip = connection[0]
	port = connection[1]
	print(f"Conexao feita pelo: {ip} e porta: {port}")
	count = 0
	while True:
		fileName = 'test.html'
		openFileName = open(fileName, 'rb')
		kar = openFileName.read(6053)
		cliente.send(kar)
		if count > 0:
			break
		print("html enviado")
    
	print(f"O cliente com: {ip} e na porta: {port} sucumbiu")
	openFileName.close()
	cliente.close()
	thread.exit()

while True:
	try: 
		cliente, ip = socketDosCria.accept()
		threading._start_new_thread(clienteNovo,(cliente, ip))
	except KeyboardInterrupt:
		print(f"Server interrompido")      
	except Exception as e:
		print(f"Erro: {e}")

socketDosCria.close()