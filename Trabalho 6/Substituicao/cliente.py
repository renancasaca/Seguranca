import socket
import pyperclip
import func
import time

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcpCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcpCliente.connect(dest)
key = 4
print 'Para sair digite exit\n'
msgEncriptada = ''
#msg =  ''

# Lendo Primeira Mensagem de Arquivo
msg = func.leArquivo2()
while msg != 'exit':
	#msgEncriptada = func.encrypt(msg,key) # para cifra de ceasar
	# copy the encrypted/decrypted string to the clipboard
	#pyperclip.copy(msgEncriptada)
	msgEncriptada = func.encrypt(msg,int(key)) # para cifra de substituicao
	print 'Encriptada pelo cliente: ',msgEncriptada
	if msg != 'exit':
		tcpCliente.send (msgEncriptada)
		time.sleep(0.2)
		print key
		tcpCliente.send (str(key))
		msg = raw_input()
tcpCliente.close()
