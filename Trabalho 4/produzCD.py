# Programa que cria o certificado digital

import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

publicKey = key.publicKey()

msg = open("Skyrim.jpg",'rb').read()
hash = SHA256.new(msg).digest()
criptHash = key.decrypt(hash)

# Escreve o arquivo criptografado a partir da imagem
arq = open("Saida.txt", "wb")
arq.write(hash)
arq.write(criptHash)
arq.write(publickey.exportKey("DER"))
