import pyperclip
 
message = 'Mensagem a ser criptografada!'

key = 2

mode = 'encrypt' # set to 'encrypt' or 'decrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
     if symbol in LETTERS:
         # get the encrypted (or decrypted) number for this symbol
         num = LETTERS.find(symbol) # get the number of the symbol
         if mode == 'encrypt':
             num = num + key
         elif mode == 'decrypt':
             num = num - key
         if num >= len(LETTERS):
             num = num - len(LETTERS)
         elif num < 0:
             num = num + len(LETTERS)
         translated = translated + LETTERS[num]

     else:
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)
