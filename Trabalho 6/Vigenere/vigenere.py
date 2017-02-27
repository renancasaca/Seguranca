import math
import os
import itertools

def EncryptV(key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	out = []
	vKey = key
	vKey = vKey.encode()
	count = 0
	for i in FileIN:	
		out.append((i + vKey[count]) % 256)
		count += 1
		if count >= len(vKey):
			count = 0
	open(fileOut,"wb").write(bytes(out))


def DecryptV(key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	out = []
	vKey = key
	vKey = vKey.encode()
	count = 0
	for i in FileIN:	
		out.append((i - vKey[count]) % 256)
		count += 1
		if count >= len(vKey):
			count = 0
	open(fileOut,"wb").write(bytes(out))


EncryptV("chave", "saida.txt", "entrada.txt")	
	
