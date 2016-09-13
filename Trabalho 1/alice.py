# Criptografia de chave pública Diffie-Hellman
# Aluno: Renan Casaca

import socket

HOST = "127.0.0.1"
PORT = 5000
#destino = ("172.20.92.123", 5000)

privateKey = int(input("Private Key: "))
generator = 5
primeModulus = 23

udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
udp.bind(origem) #Vincula um endereço endereço IP e porta, no socket
while True:
	msg, cliente = udp.recvfrom(1024)
	#print ("Recebido",msg+" de", cliente)
	msgRecived = msg.decode('utf-8')
	print(cliente, msgRecived)
	#sharedKey = ((msgRecived**privateKey) % primeModulus)
	#msg = str(((generator**privateKey) % primeModulus))
	#udp.sendto(msg,destino)
	#print("Shared Key:",sharedKey)
print ("Finalizando conexao com", cliente)
udp.close()


##generator = 5
##primeModulus = 23

# Private Random Number
##privateNumber = int(input("PRN: "))

##print((generator**privateNumber) % primeModulus)

##result = int(input("Public Result: "))

##print("Key:",(result**privateNumber) % primeModulus)
