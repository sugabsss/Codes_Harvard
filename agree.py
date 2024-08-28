import sys

#Criando meu array de tentativas;
tentar = [
    {"tentativas": "Apenas 4 tentativas restantes!"},
    {"tentativas": "Apenas 3 tentativas restantes!"},
    {"tentativas": "Apenas 2 tentativas restantes!"},
    {"tentativas": "Apenas 1 tentativa restante!"},
]

def obter_resposta():
    resposta = input("Do you agree? (y/n)\n").lower().strip()         #Pegando respostas do usuario;
    return resposta

def main():
    resposta = obter_resposta()
    
    if resposta in ["y","yes"]:
        print("Agreed!")
        sys.exit(0)
        
    elif resposta in ["n","no"]:
        print("Not Agreed!")
        sys.exit(0)

    else:
        j = 0
        
    while j < 4:
        for i in tentar:    
            j += 1

            print("Only yes or no Answers!")
            print (i["tentativas"])
            
            resposta = input("Do you agree?\n")
            
            if resposta in ["y","yes"]:
                print("Agreed!")
                sys.exit(0)
            
            elif resposta in ["n","no"]:
                print("Not Agreed!")
                sys.exit(0)
        break
    
    print ("Excesso no numero de tentativas!\nTente novamente mais tarde") 
    sys.exit(1)

main()
