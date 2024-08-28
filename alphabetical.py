import sys

frase = input("Digite uma frase para contagem:")
tamanho = len(frase)
if tamanho > 30:
    print("Limite máximo 30 caracteres")
    sys.exit(1)
else:
    print(f"Tamanho da frase: {tamanho}")
    sys.exit(0) 
 