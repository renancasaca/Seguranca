def encrypt(msg,key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ' '
    msg = msg.upper()
    for symbol in msg:
     if symbol in LETTERS:

         num = LETTERS.find(symbol) # get the number of the symbol
         num = num + key


         if num >= len(LETTERS):
             num = num - len(LETTERS)
         elif num < 0:
             num = num + len(LETTERS)

         translated = translated + LETTERS[num]

     else:
        translated = translated + symbol
    return translated

def decrypt(msg,key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ' '
    msg = msg.upper()
    for symbol in msg:
     if symbol in LETTERS:

         num = LETTERS.find(symbol) # get the number of the symbol
         num = num - key


         if num >= len(LETTERS):
             num = num - len(LETTERS)
         elif num < 0:
             num = num + len(LETTERS)

         translated = translated + LETTERS[num]

     else:
        translated = translated + symbol
    print 'Texto Original: ',translated
    return translated
    
def searchKey(original,encriptada):
    l1 = ord(original[2])
    l2 = ord(encriptada[1])
    key = l2-l1
    print 'Valor da chave: ',key
    #return translated
    
def encryptSub(texto, key):
	encrypt=''
	for i in range(0,key):
		if i==0: 
			cont = i
		for j in range(i,len(texto)):
			if j == i:
				j = i
			elif j != 0:
				j = back
			encrypt = encrypt + texto[j]
			cont = cont + 1
			j = j + (key)
			back = j
			if j >= len(texto):
				j = i + 1
				break
			if cont == len(texto)-1:
				encrypt = encrypt + texto[j]
			if cont >= len(texto)-1:
				print encrypt
				return encrypt
		
def decryptSub(msg,key):
	translated = ''
	print msg
	vet = ((len(msg))/key) + 1
	for i in range(0,vet):
		if i==0: 
			cont = i
		for j in range(i,len(msg)):
			if j == i:
				j = i
			elif j != 0:
				j = ant
			translated = translated + msg[j]
			cont = cont + 1
			j = j + vet
			ant = j
			if j > len(msg):
				j = i + 1
				break
			if cont >= len(msg):
				print 'Mensagem traduzida: ',translated
				return translated
def leArquivo():
	letter = 'abcdefghijklmnopqrstuvwxyz123456789'
	f = open("msgcliente.txt","r")
	for linha in f:
		nova = ''
		print linha.rstrip()
		print len(linha)
		for i in range(0,len(linha)):
			if linha[i] in letter:
				nova = nova + linha[i]
		return nova
	f.close()

def leArquivo2():
	f = open("msgcliente.txt","r")
	msg = f.readline()
	msg = msg.split(".")
	msg_c = msg[0]
	print 'Retornando ', msg_c
	return msg_c


def encryptSub1(texto, key):

        cifrado = ''
        texto = texto.replace(' ', '-')
 
        qtd_ch = len(texto)
        col = qtd_ch // key
        if qtd_ch % key > 0:
            col += 1
 

        i = 0
        while len(texto) < key * col:
             texto += "$"
             i += 1
        for i in range(col):
             for j in range(0, qtd_ch, col):
                 cifrado += texto[i + j]
        return cifrado.upper()


def decryptSub1(texto, key):
        texto_plano = ''
        texto = texto.replace(' ', '-')
        for i in range(key):
            for j in range(0, len(texto), key):
                texto_plano += texto[i + j]
        texto_plano=texto_plano.replace('-', ' ')
        texto_plano=texto_plano.replace('$', '')                
        return texto_plano.upper()
