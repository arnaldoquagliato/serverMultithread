import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
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


def newClient(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"Conexao feita pelo: {ip}e porta: {port}")
	count = 0
	while True:
		if count == 120:
			break
		print(f"estou executando: {count}")
		count +=1
	print(f"O cliente com: {ip}e na porta: {port} sucumbiu")
	client.close()

while True:
	try: 
		client, ip = socketDosCria.accept()
		threading._start_new_thread(newClient,(client, ip))
	except KeyboardInterrupt:
		print(f"Server interrompido")
	except Exception as e:
		print(f"Erro: {e}")

socketDosCria.close()