"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""

def xor_cipher(string, key): 
#данную функцию можно использовать как для шифрования, так и для дешифрования
    cipher_string = ""    #создаю новую пустую строку
    for symbol in string:
        cipher_string += chr(ord(symbol) ^ key)   #преобразование символа в число из ASCII, затем использование XOR, преобразование числа в соответствующий ему символ из ASCII и занесение этого символа в пустую строку
    return cipher_string
    
string = str(input("Input string: "))
key = int(input("Input key: "))
encoded = xor_cipher(string, key)
print("Encoded string: ", encoded)
decoded = xor_cipher(encoded, key)
print("Decoded string: ", decoded)

