def main():
    x = int(input("Valor de x:"))
    y = int(input("Valor de y:"))
    z = input("escolha a operação a ser realizada:('+','-','/','*'\n)")
    resultado = operador(x,y,z)
    print(f"Total:{resultado}")

def operador (x,y,z):
    if z == '+' :
        return x + y
    elif z == '-' :
        return x - y
    elif z == '*' :
        return x * y
    elif z == '/' :
        return x / y
    else:
        print("Digite um operador Válido!")
        return None
main()