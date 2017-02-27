# Cifra de Transposicao

import math
import os
import itertools

def EncryptT(func, key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	fileSize = os.path.getsize(fileIn)
	cols = math.ceil(fileSize / key)	
	
	matrix = [ [] for x in range(key)]
	
	count = 0
	left = cols - (fileSize % cols)
	FileIN = list(FileIN) + [0] * left
	for i in FileIN:
		matrix[count].append(i)
		count += 1
		if count >= key:
			count = 0
	out = []
	for i in matrix:
		for j in i:
			out.append(j)
	open(fileOut,"wb").write(bytes(out))


def DecryptT(func, key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	fileSize = os.path.getsize(fileIn)
	cols = math.ceil(fileSize / key)
	
	matrix = [ [] for x in range(cols)]
	
	count = 0
	if func == 'e':		
		left = cols - (fileSize % cols)
		FileIN = list(FileIN) + [0] * left
	for i in FileIN:
		matrix[count].append(i)
		count += 1
		if count >= cols:
			count = 0
	out = []
	for i in matrix:
		for j in i:
			out.append(j)
	open(fileOut,"wb").write(bytes(out))

#Chamadas
EncryptT(15, "in.txt", "out.txt")
DecryptT(15, "out.txt", "in2.txt") 
