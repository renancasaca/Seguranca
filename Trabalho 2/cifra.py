from Crypto.Cipher import AES

key = "This is a key123" # 256 bytes (AES256)
IV = 16* "\x00" # Vetor de inicialização (Salt)
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV)

text = "j" * 64 + "i" * 128
print("Texto normal:", text)
print()
ciphertext = encryptor.encrypt(text)
print("Texto encriptado:", ciphertext)



