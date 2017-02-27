# Programa que verifica o certificado digital

import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

arq = open("Saida.txt", "rb")
hash = arq.read(32)
criptHash = arq.read(128)
publicKey = arq.read(162)
key = RSA.importKey(publicKey)

if key.encrypt(criptHash,1024)[0] == hash:
    print("Ok")
else:
    print("Chave incorreta")

# Cria chave aleatória para testar chave inválida
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publicKey = key.publickey()

if publicKey.encrypt(criptHash,1024)[0] == hash:
    print("Chave valida!")
else:
    print("Chave invalida!")

