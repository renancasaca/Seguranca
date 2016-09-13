import socket

HOST = "127.0.0.1"
PORT = 5000

privateKey = int(input("Private Key: "))
generator = 5
primeModulus = 23 

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT) # Endereço do destino
#tcp.connect(destino)
#msg = bytes(((generator**privateKey) % primeModulus)) # Converte o dado em bytes para enviar pelo socket
msg = str(((generator**privateKey) % primeModulus))
msgtoSend = msg.encode('utf-8')
udp.sendto(msgtoSend, destino) 
#while True:
#	msg = conexao.recv(1024)
#	if not msg:
#		break
#	msgRecived = msg.decode('utf-8')
#	sharedKey = ((msgRecived**privateKey) % primeModulus)
#print("Shared Key:",sharedKey)
udp.close()


