import hashlib

while True:
    string = input("Digite uma string para gerar o hash: ")
    
    gerar_hash = hashlib.sha1()
    gerar_hash.update(string.encode())
    
    imprimir_hash_hexdigest = gerar_hash.hexdigest()
    
    print(f"O hash SHA-1 da string '{string}' é: {imprimir_hash_hexdigest}")
