# Criptografia de chave pública Diffie-Hellman
generator = 5
primeModulus = 23

# Private Random Number
privateNumber = int(input("PRN: "))

print((generator**privateNumber) % primeModulus)

result = int(input("Public Result: "))

print("Key:",(result**privateNumber) % primeModulus)
