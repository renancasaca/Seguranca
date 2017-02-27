import socket
import func

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcpServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcpServidor.bind(orig)
tcpServidor.listen(1)
encriptada = ''
while True:
    con, cliente = tcpServidor.accept()
    print 'Conectado por', cliente
    while True:	
		encriptada = con.recv(1024)
		if not encriptada: break
		print cliente, encriptada
		key = con.recv(1024)
		print cliente, key
		#original = func.decrypt(encriptada,int(key)) # para cifra de ceasar
		original = func.decrypt(encriptada,int(key)) # para cifra de transposicao
		print 'Original: ', original
		#con.send('Aguardando a chave...\n')
		#func.searchKey(original,encriptada)
		f = open("msgServidor.txt", "a") #Abre arquivo para gravar
		f.writelines(original) #Grava a mensagem original enviada pelo cliente no arquivo
		f.writelines("\n")
    print 'Finalizando conexao do cliente', cliente
    con.close()
