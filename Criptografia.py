from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import ast

def gerar_chave():
    while True:
        chave = get_random_bytes(24)
        if DES3.adjust_key_parity(chave):
            break
    return chave

def criptografar(mensagem, chave):
    iv = get_random_bytes(8) 
    cipher = DES3.new(chave, DES3.MODE_CBC, iv)
    mensagem_padded = pad(mensagem.encode(), DES3.block_size)
    criptografado = iv + cipher.encrypt(mensagem_padded)
    return criptografado

def descriptografar(criptografado, chave):
    iv = criptografado[:8]
    cipher = DES3.new(chave, DES3.MODE_CBC, iv)
    mensagem_padded = cipher.decrypt(criptografado[8:])
    mensagem = unpad(mensagem_padded, DES3.block_size)
    return mensagem.decode()

if __name__ == "__main__":
    mensagem = input("Mensagem a Criptografar: ")
    chave = gerar_chave()  

    mensagem_criptografada = criptografar(mensagem, chave)
    print(f"Mensagem Criptografada: {mensagem_criptografada}")

    decriptografar = input("Deseja decriptografar? ").strip().lower()

    if decriptografar == "sim":
        mensagem_decrip = input("O que deseja decriptografar? ")

        mensagem_decrip_bytes = ast.literal_eval(mensagem_decrip)

        mensagem_descriptografada = descriptografar(mensagem_decrip_bytes, chave)
        print(f"Mensagem Descriptografada: {mensagem_descriptografada}")


