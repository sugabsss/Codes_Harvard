import csv 
import sys

candidatos = []

def votos_update(): 
    try:
        with open("candidatos.csv", mode = 'r') as file:
            
            reader = csv.DictReader(file)
            global candidatos
            for row in reader:
                row["Quantidade de votos"] = int (row["Quantidade de votos"])
                candidatos.append(row)

                for candidato in candidatos:
                    print(f"Candidato:{candidato['nome']}, Quantidade de votos:{candidato['Quantidade de votos']}")
    
    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return 1
    except Exception as e:  
        print("Error ao ler arquivo:{e}")
        return 1

def votos_salvar():
    fieldnames = ['nome',"Quantidade de votos"]

    try:
        with open("candidatos.csv", mode = 'w') as file:
            write = csv.DictWriter(file, fieldnames=fieldnames)
            write.writeheader()
            write.writerows(candidatos)
            print("Dados Atualizados com sucesso!")
            
    except FileNotFoundError:
        print("Error 404 FIle not FoundError")
        return 1
    
    except Exception as e:  
        print("Error ao ler arquivo:{e}")
        return 1
    

def limite_letra()-> bool:
    letra = input("Escolha o candidato de acordo com a respectiva letra:\n------> a : Carlos <------\n------> b : Paulo <------\n------> c : Maria <------\n Clique enter para confirmar\n").lower().strip()

    if letra < 'a' or letra > 'c':
        print("Erro Selecione um candidato válido")

    return letra

def main():
    if votos_update() == 1:
        sys.exit(1)

    letra = limite_letra()
    if letra is None:
        sys.exit(1)


    if letra == 'a':
        candidatos[0]["Quantidade de votos"] += 1
        print(f"Candidato votado: {candidatos[0]['nome']}\nNúmero de votos: {candidatos[0]['Quantidade de votos']}")

    elif letra == 'b':
        candidatos[1]["Quantidade de votos"] += 1
        print(f"Candidato votado: {candidatos[1]['nome']}\nNúmero de votos: {candidatos[1]['Quantidade de votos']}")
        

    elif letra == 'c':
        candidatos[2]["Quantidade de votos"] += 1
        print(f"Candidato votado: {candidatos[2]['nome']}\nNúmero de votos: {candidatos[2]['Quantidade de votos']}")

    vencer = max(candidatos, key=lambda c: c["Quantidade de votos"])
    if vencer["Quantidade de votos"] > 10:
        print(f"O Candidato Vencedor foi : {vencer['nome']}")
    
    if votos_salvar() == 1:        
        sys.exit(1)

    sys.exit(0)

main()


        