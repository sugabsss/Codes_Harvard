
def main (): 
    numero = list(range(1,27))
    letras = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    letra = input("------- > Nos de uma letra e ganhe um numero :) < -------\n").lower().strip()
   
    if letra < 'a' or letra > 'z':
        print("> Desculpe letra ultrapassou o contador XD <\n Por favor digite um letra entre 'a' - 'z' ")
        return 
    
   

    if letra in letras:
        numero = ord(letra) - ord('a') + 1           
        print(f"{numero}")
      
main()