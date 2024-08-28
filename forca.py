import sys

def palavra_forca():
    try:
        while True:
            print("»»»»»» Vamos Jogar O Jogo da Forca! ««««««")
            pergunta = input("Insira a Palavra da forca: ")
            return pergunta
    except ValueError as e:
        print(f"Error{e}: Insira uma palavra válida")

def resposta_forca():
    try:
        while True:
            letras = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            letra = input("Insira uma letra de 'a' até 'z': ")

            if letra < 'a' or letra > 'z':
                print("Valor invalido!")
                sys.exit(1)

            if letra in letras:
                print(f"Letra selecionada: {letra}")
                break

    except ValueError as e:
        print(f"Error{e}: Insira uma palavra válida")
    
def main():
    palavra = palavra_forca()
    resposta = resposta_forca()

