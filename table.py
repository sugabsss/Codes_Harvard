import sys

def main():
    i = 0
    for i in range(3):
        i += 1
        tamanho = (input("Verificador de Caracteres :"))
        n = len(tamanho)
        print(f"Tamanho:{n}")
        if i == 3:
            sys.exit(0)
main ()