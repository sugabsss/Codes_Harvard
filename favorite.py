#Iremos Criar uma lista e de cores favoritas;

import csv, sys

lista_cores = []

def cores_favoritas():
    try:
        with open("favoritos.csv", mode='r')as file:
            reader = csv.DictReader(file)
            global lista_cores

            for row in reader:
                lista_cores.append(row)
                row["cores"] = (row["cores"])
  
    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return  
        
def salvar_cor():
    fieldnames = ['cores']

    try:
        with open("favoritos.csv", mode = 'w', newline='') as file:
            write = csv.DictWriter(file, fieldnames=fieldnames)
            write.writeheader()
            write.writerows(lista_cores)
            print("-----»»»»»»    Dados Atualizados    ««««««-----")

    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return   

def selecionar_cor():
    selecionar = input("Nos conte sua cor favorita para uma pesquisa...\n")
        
    return {'cores':selecionar}

def main():
    if cores_favoritas() == 1:
        sys.exit(1)
    
    cor = selecionar_cor()

    lista_cores.append(cor)
    print(f"-----»»»»»» Cor selecinada ««««««-----\n{cor['-------------cores-------------']}\n")

    if cor is None:
        sys.exit(1)

    if salvar_cor() == 1:
        sys.exit(1)
    
    sys.exit(0)
main()